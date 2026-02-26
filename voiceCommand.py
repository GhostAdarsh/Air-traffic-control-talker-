# import modules here 
import Vosk 
aircraft_list = [] 
holding_points = []

class VoiceControl: 

    def __init__(self):
        self.activeAirctaft = aircraft_list
        self.valid_holding_points = holding_points
    
    def process_voice(self):
        text = self.recognise_commad() 
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
        pass 
    def parse_command(self, text): 
        pass
    def execute_command(self, command):
        pass
    def computer_voice(self, message): 
        pass 
     



print("hello world")
