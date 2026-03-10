# import modules here 
import vosk 
import pyaudio
import queue 
#import sounddevice as sd 
import json 
from vosk import Model, KaldiRecognizer



#load model 
#print("hell0")
        # test data: 
test_input = "speedbird one two three cleared for takeoff runway two seven"
test_input2 = "speedbird one two thee taxi to holding point cobra"
q = queue.Queue() 

aircraft_list = ["speedbird123"] 
# coordinates for the holding points (checkpoints): 
checkpts = [(384, 358), (320,340), (448,345), (417,338), (326,374), (344,502), (374, 502), (393,483)]
holding_points = {
    "dasso": [384,358],
    "snapa": [320,340],
    "rando": [448,345], 
    "vikas": [417,338],
    "cobra": [326,374], 
    "oster": [393,483] 
    }





class VoiceControl: 

    def __init__(self):
        self.activeAirctaft = aircraft_list
        self.valid_holding_points = holding_points

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

        command  = {
            "callsign": None,
            "action": None,
            "runway": None, 
            "holding_point": None 
        }
        ## action words 
        if "takeoff" in words: 
            command["action"] = "takeoff"
            print("aciton - takeoff")

        elif "taxi" in words: 
            command["action"] = "taxi"
            print("action - taxi")

        elif "hold" in words: 
            command["action"] = "hold"
            print("action - hold")

        # callsign 
        for aircraft in self.activeAirctaft: 
            airline = ''.join([c for c in aircraft if not c.isdigit()])

            if airline in text: 
                command["callsign"] = aircraft
        
     

        # runway numbers 
        if "runway" in words: 

            i = words.index("runway")
            
            if i + 2 < len(words): 
                first = words[i+1]
                second = words[i+2]

                if first in number_map and second in number_map: 
                    command["runway"] = number_map[first] + number_map[second]
        ## holding points
        for point in self.valid_holding_points: 
            
            if point in words:
                command["holding_point"] = point

        
        print(command)




    def execute_command(self, command):
        pass
    def computer_voice(self, message): 
        pass 




print("hello world")
print("this is to be done by monday")

#VoiceControl.recognise_command()

voice = VoiceControl() 
#print(voice.recognise_command())
result = voice.parse_command(test_input2)

