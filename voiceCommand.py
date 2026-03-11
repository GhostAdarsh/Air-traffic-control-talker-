# import modules here 
import vosk 
import pyaudio
import queue 
import sounddevice as sd 
import json 
from vosk import Model, KaldiRecognizer

#import pathfinding 
import pathfinding
from pathfinding import Pathfinder 
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
        



#load model 
#print("hell0")
        # test data: 
test_input = "speedbird one two three cleared for takeoff runway two seven"
test_input2 = "speedbird one two thee taxi to holding point cobra"
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

    def __init__(self, pathfinder):
        # prerequisites: 
        self.activeAirctaft = aircraft_list
        self.valid_holding_points = {}
        self.pathfinder = pathfinder
          
        # dictionary
        self.valid_holding_points = {
            "dasso": [384,358],
            "snapa": [320,340],
            "rando": [448,345], 
            "vikas": [417,338],
            "cobra": [326,374], 
            "oster": [393,483] 
        }

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
            "zero": "0",
            "one": "1", 
            "two": "2", 
            "three": "3", 
            "four": "4", 
            "five": "5", 
            "six": "6", 
            "seven": "7", 
            "eight": "8", 
            "nine": "9"
        }
        
        #standardises the text 
        text = text.lower().strip() 
        words = text.split() 

        # TROUBLE SHOOTING NUMBER MAP: 
        callsign_number = ""
        for word in words: 
            if word in number_map: 
                callsign_number += number_map[word]

        command  = {
            "callsign": None,
            "action": None,
            "runway": None, 
            "holding_point": None, 
            "destination": None 
            
        }
        # callsign and callsign number
        
        for aircraft in self.activeAirctaft: 
            airline = ''.join([c for c in aircraft if not c.isdigit()])

            if airline in words: 
                command["callsign"] = aircraft
            
            index = words.index("speedbird")

            if index + 1 < len(words):
                number = words[index + 1]
                command["callsign"] = f"speedbird{number}"

            for word in words: 

                if word.startswith("speedbird"):
                    number = word.replace("speedbird", "")
                    command["callsign"] = f"speedbird{number}"

            if callsign_number: 
                command["callsign"] = "speedbird" + callsign_number

        ## action words 
        if "takeoff" in words: 
            command["action"] = "takeoff"
            print("action - takeoff")
            
        elif "taxi" in words: 
            command["action"] = "taxi"
            print("action - taxi")

        elif "hold" in words: 
            command["action"] = "hold"
            print("action - hold")

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
            print(command)
            return command 
        
        return None 
    

        
       
    



    def execute_command(self, command, planes):
        # extracting intel 
        callsign = command["callsign"]
        action = command["action"]
        destination_name = command["destination"]
        self.pathfinder = pathfinding
        self.callsign = callsign
        planes = []

        # finding aircraft in list 
        plane = None 

        for p in planes: 
            if p.callsign == callsign: 
                plane = p 
                break
        if plane is None: 
            print("aircraft noit found")
            return 
        
        #plen  // ALMOST THERE JUST NEED TO WORK ON EXECUTE AND MAIN.PY - FINISH THIS IN SCHOOL!
        # convert holding points to coordinates: 
        destination = self.valid_holding_points[destination_name]

        # taxi commands 
        if action == "taxi": 

            start = self.plane.grid_position # need to add the starting point list pts
            end = destination

            path = self.pathfinder.create_path(start, end)

            self.plane.set_path(path)

            print(f"{callsign} taxiing to {destination_name}")




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

voice = VoiceControl()

voice.pathfinder = FakePathfinder()

voice.execute_command(command, planes)




