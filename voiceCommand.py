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
test_input = "plane take of at the area of the top left"
test_input2 = "123 takeoff runway 27L"
final_test = "speedbird one two three"
q = queue.Queue() 

aircraft_list = ["speedbird123"] 
# coordinates for the holding points (checkpoints): 
checkpts = [(384, 358), (320,340), (448,345), (417,338), (326,374), (344,502), (374, 502), (393,483)]

## creat eplanes
#plane1 = Plane("speedbird12", (384,358))

#planes = [plane1]

# create a fake command: 
'''
command = {
    "callsign": "speedbird12",
    "action": "taxi", 
    "destination": "horka"
}'''
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
        self.vocab = ["takeoff", "runway", "hold", "taxi", "holding point", "zero", "one", "two", "three", "four", "speedbird", "five", "six", "seven", "eight", "nine", ]
        #recogniser looks for self.vocab - to brush off unfiltered words 
        self.recogniser = KaldiRecognizer(self.model, 16000, json.dumps(self.vocab))
        # test data: 
        test_input = "speedbird one two three cleared for takeoff runway two seven"
        # creatubg a queue
        self.q = queue.Queue()
        # sending test input for parsing
        #parsed = self.parse_command(test_input)
        #print(parsed)

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
                    print(text)
                    #Audio input: “Speedbird one two three cleared for take off runway 27” 
                    return self.parse_command(text)
                    # TESTING CONST + recognise_command()
                    # output: works as expected  - NOW testing wiht no audio input  - didnt speak for 10 seconds - did not recognise a thing 

## main processing 
   #main voice processing logic 
    def process_voice(self):
        text = self.recognise_command() 
        print(text)
        teast_2 = "speedbird123 taxi to holding point horka"
        if not text: 
            self.computer_voice("Repeat")
            return
        
        command = self.parse_command(teast_2)
        #print(command)
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
        print("parsed command:", command)

        # validate command 
        if command["callsign"] and command["action"] and command["destination"]: 
            #print(command)
            return command 
        
        return command
    
    def execute_command(self, command, planes):
        # extracting intel 
        callsign = command["callsign"]
        action = command["action"]   

        for plane in planes: 
            if plane.callsign != callsign: 
                continue

            #print(f"plane matched:{plane.callsign}")

            
            
            # taxi to holding pt 
            if action == "taxi": 
                dest_name = command["destination"]
                destination = self.valid_holding_points[dest_name]
            # takeoff - fixed runway coordinate: 
            elif action == "takeoff": 
                runway_coords = {
                    "27": (41,38), 
                    "09": (68,43)
                }
                runway = command.get("runway", "27") # default
                destination = runway_coords[runway]
            else: 
                #print(f"Unkown action: {action}")
                return 
            start_pos = plane.grid_position
            start_pos = tuple(start_pos)
            destination = tuple(destination)
            return start_pos, destination

    
    def computer_voice(self, message): 
        pass 


planes = []

print("hello world")
# ommand 
command = {
    "callsign": "speedbird123", 
    "action": "takeoff", 
    "runway": "27", 
    "holding_point": None,
    "destination": None
}

plane = Plane("speedbird123", (0,0),)
planes.append(plane)
#voice = VoiceControl() 
#voice.pathfinder = FakePathfinder()
#voice.valid_holding_points = {"horka": (10,20)}
## still and issue - nneds sorting out before, IT NEEDS TO OUTPUT COORDINATES AND PATHS - THAT WILL BE INPUTTED IN TO THE PATHFINDER!!!
#voice.execute_command(command, planes)

#MODULAR TESTINGS: 
voice = VoiceControl() 
voice.recognise_command()
 
