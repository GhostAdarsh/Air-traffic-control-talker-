# import modules here 
import vosk 
import pyaudio
import queue 
import sounddevice as sd 
import json 
from vosk import Model, KaldiRecognizer

#load model 
model = Model("vosk-model-smallen-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

q = queue.Queue() 

aircraft_list = [] 
holding_points = []

class VoiceControl: 

    def __init__(self):
        self.activeAirctaft = aircraft_list
        self.valid_holding_points = holding_points
    
    def process_voice(self):
        text = self.recognise_command() 
        if not text: 
            self.computer_voice("Repeat")
            return
        command = self.parse_command(text)
        if not command: 
            self.computer_voice("Invalid Command")
            return text
            return 
        
        self.execute_command(command)

    def recognise_command(self):
        print("Listening...")
        while True: 
            data = self.q.get() 
            if self.recognizer.AcceptWaveform(data): 
                result = json.loads(self.recognizer.Result()) 
    def parse_command(self, text): 
        pass
    def execute_command(self, command):
        pass
    def computer_voice(self, message): 
        pass 




print("hello world")
print("this is to be done by monday")

