# import modules here 
import vosk 
import pyaudio
import queue 
import sounddevice as sd 
import json 
from vosk import Model, KaldiRecognizer

#import pathfinding 
import pathfinding
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


#TESTINGS: 
class FakePathfinder: 
    def create_path(self, start, end): 
        print("pathfinder called ")
        print("start:",  start)
        print("end:", end)

        return [(start), (end)]

class Plane: 

    def __init__(self, callsign, grid_position):
        self.callsign = callsign
        self.grid_position = grid_position
        self.path = [] 

    def set_path(self,path): 
        self.path = path 
        print("pathset:", path)
        
## TEST PLANE: 
plane = Plane("speedbird12", (0,0))
planes = [plane]



#load model 
#print("hell0")
        # test data: 
test_input = "speedbird one two three cleared for takeoff runway two seven"
test_input2 = "speedbird one two thee taxi to holding point cobra"
final_test = "speedbird one two three"
q = queue.Queue() 

aircraft_list = ["speedbird123"] 
# coordinates for the holding points (checkpoints): 
checkpts = [(384, 358), (320,340), (448,345), (417,338), (326,374), (344,502), (374, 502), (393,483)]

## creat eplanes
plane1 = Plane("speedbird12", (384,358))

planes = [plane1]

# create a fake command: 
command = {
    "callsign": "speedbird12",
    "action": "taxi", 
    "destination": "horka"
}
## FAKE TEST S edit this later!!!! 
class VoiceControl: 

    def __init__(self):
        # prerequisites: that will be assigned from main.py: 
        self.valid_holding_points = {} 
        self.activeAircraft = aircraft_list
        self.pathfinder = None
        #fake holding points: 
        
          
        # dictionary
        '''self.valid_holding_points = {
            "dasso": [384,358],
            "snapa": [320,340],
            "rando": [448,345], 
            "vikas": [417,338],
            "cobra": [326,374], 
            "oster": [393,483] 
        }'''


        # intialising vosk 
        self.model = Model("vosk-model-small-en-us-0.15")
        # list of words 
        self.vocab = ["takeoff", "runway", "hold", "taxi", "holding point"]
        #recogniser 
        self.recogniser = KaldiRecognizer(self.model, 16000, json.dumps(self.vocab))
        # test data: 
        test_input = "speedbird one two three cleared for takeoff runway two seven"
        # creatubg a queue
        self.q = queue.Queue()
        # sending test input for parsing
        parsed = self.parse_command(test_input)
        print(parsed)

        def callback(indata, frames, time, status):
            self.q.put(bytes(indata))

        self.stream = sd.RawInputStream(
            samplerate= 16000, 
            blocksize= 8000, 
            dtype= 'int16', 
            channels= 1,
            callback=callback
        )

        self.stream.start()

    def recognise_command(self):
        
        # setting the audio specifics  
        print("listening")

            # starts recognising the voice from mic
        while True: 
            data = self.q.get() 

            if self.recogniser.AcceptWaveform(data): 
                    result = json.loads(self.recogniser.Result())
                    text =  result.get("text", "")
                    text = text.strip().lower() 
                    return self.parse_command(text)

## main processing 
    def process_voice(self):
        text = self.recognise_command() 
        print(text)

        if not text: 
            self.computer_voice("Repeat")
            return
        
        command = self.parse_command(text)
        if not command: 
            self.computer_voice("Invalid Command")
            return text
            return 
        
        self.execute_command(command)

    
    def parse_command(self, text):
        # prerequisite dictionaries: 
        number_map = {
            "zero": "0","one": "1", "two": "2", "three": "3", "four": "4", 
            "five": "5", "six": "6", "seven": "7", 
            "eight": "8", "nine": "9"
        }
        
        #standardises the text 
        text = text.lower().strip() 
        words = text.split() 

        # TROUBLE SHOOTING NUMBER MAP: 
        '''callsign_number = ""
        for word in words: 
            if word in number_map: 
                callsign_number += number_map[word]'''

        command  = {
            "callsign": None,
            "action": None,
            "runway": None, 
            "holding_point": None, 
            "destination": None 
            
        }
        
        # callsign and callsign number
        for i, word in enumerate(words): 
            # only one case: 

            if word == "speedbird": 
                number = ""
                j = i + 1
                while j < len(words) and words[j] in number_map: 
                    number += number_map[words[j]]
                    j += 1
                if number: 
                    command["callsign"] = f"speedbird{number}"
                    break


        ## action words 
        if "takeoff" in words: 
            command["action"] = "takeoff"
        elif "taxi" in words: 
            command["action"] = "taxi"
        elif "hold" in words: 
            command["action"] = "hold"
            

        # runway numbers 
        if "runway" in words: 
            i = words.index("runway")
            if i + 2 < len(words): 
                first = words[i+1]
                second = words[i+2]
                if first in number_map and second in number_map: 
                    command["runway"] = number_map[first] + number_map[second]

        ## holding points / destination 
        for point, coords in self.valid_holding_points.items():
            if point.lower() in words: 
                command["destination"] = coords
                break

        # print WHOLE command: 
        #print("parsed command:", command)

        # validate command 
        if command["callsign"] and command["action"] and command["destination"]: 
            print(command)
            return command 
        
        return command
    
    def execute_command(self, command, planes):
        # extracting intel 
        callsign = command.get("callsign")
        action = command.get("action")
        
        for plane in planes: 
            if plane.callsign != callsign: 
                continue

            print(f"plane matched:{plane.callsign}")

            # taxi to holding pt 
            if action == "taxi": 
                destination_name = command.get("destination")
                destination = self.valid_holding_points[destination_name]

            # takeoff - fixed runway coordinate: 
            elif action == "takeoff": 
                runway_coords = {
                    "27": (41,38), 
                    "09": (68,43)
                }
                runway = command.get("runway", "27") # default
                destination = runway_coords.get(runway, (41,38))
            else: 
                print(f"Unkown action: {action}")
                return 
            # get path 
            path = self.pathfinder.create_path(plane.grid_position, destination)
            print(path)
            # ensure that plath is a lsit of tuples: 
            if isinstance(path[0], int): 
                path=[tuple(path)]
            plane.set_path(path)
            
    
    def computer_voice(self, message): 
        pass 




#print("hello world")
#print("this is to be done by monday")

#VoiceControl.recognise_command()
# HAV ENO IDEA WHATS DONE HERE
#voice = VoiceControl(aircraft_list=aircraft_list, holding_points=checkpts, pathfinder= pathfinding) 
#print(voice.recognise_command())
#result = voice.parse_command(test_input2)
#result = voice.execute_command(test_input)
# tests: 
#voice = VoiceControl()
#voice.pathfinder = FakePathfinder()
#voice.execute_command(command, planes)


plane = Plane("speedbird12", (0,0))
planes = [plane]
#voice = VoiceControl() 
#voice.pathfinder = FakePathfinder()
#voice.valid_holding_points = {"horka": (10,20)}


#command = {"callsign": "speedbird12", "action": "takeoff","runway": "27", "destination": "horka"}


#print("planes list:", [p.callsign for p in planes])


#text = "speedbird12 taxi horka"

#command = voice.parse_command(test_input2)

#voice.execute_command(command, planes)


## IDEK ANYMORE - JUST END IT  
pathfinder = None
voice = VoiceControl()
voice.activeAircraft = aircraft_list
voice.pathfinder = None 
