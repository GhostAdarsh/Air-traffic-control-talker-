# import modules here 
import vosk 
import pyaudio
import queue 
import sounddevice as sd 
import json 
from vosk import Model, KaldiRecognizer

#load model 
#print("hell0")

q = queue.Queue() 

aircraft_list = [] 
holding_points = []

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
        test_input = "speedbird one two three crealed takeoffrunway two seven"

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
            

                    valid_words = [] 

                    for command in self.vocab: 
                        if command in text: 
                            valid_words.append(command)

                    '''if valid_words: 
                        print("VALID commmand:", valid_words)
                        return valid_words
                    else: 
                        print("invalid", text)
                        return None'''


                    
                    if text != "":
                        print("recognised", text)
                        return text
            
     
    

                





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
        #standardises the text 
        text = text.lower().strip() 
        words = text.split() 

        command  = {
            "callsign": None,
            "action": None,
            "runway": None, 
            "holding_point": None 
        }
        if "takeoff" in words: 
            command["action"] = "takeoff"
            print("aciton - takeoff")

        elif "taxi" in words: 
            command["action"] = "taxi"
            print("action - taxi")

        elif "hold" in words: 
            command["action"] = "hold"
            print("action - hold")


    def execute_command(self, command):
        pass
    def computer_voice(self, message): 
        pass 




print("hello world")
print("this is to be done by monday")

#VoiceControl.recognise_command()

voice = VoiceControl() 
print(voice.recognise_command())
