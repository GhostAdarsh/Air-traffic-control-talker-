'''print("hello world")
# nat lang processing? ?? 

import spacy 
import nltk 
nltk.download('punkt')
import speech_recognition as sr 
from nltk.tokenize import sent_tokenize, word_tokenize
r = sr.Recognizer() 
example_string = "Muad'Dib learned rapidly because his first training was in how to learn"

# tokenise string: 
sent_tokenize(example_string)

aims - find text to analyse (this will be voice input)
preprocess text for analysis 

analyse text 

and then come up with a solution (in game movements)


'''


#from nltk.tokenize import sent_tokenize, word_tokenize 

#example_string = "Muad'Dib learned rapidly because his first training was in how to learn."
#sent_tokenize(example_string)


import speech_recognition as sr 
import pyaudio
import pyttsx3
import google

'''

def icao_input(recognizer, microphone):

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Adjusting for ambinet noise")
        r.adjust_for_ambient_noise(source)
        print("say smthn!")
        audio = r.listen(source)


icao_input()

'''

recognizer = sr.Recognizer()

while True: 
    try: 

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration= 0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_bing(audio)
            text = text.lower()

            print("Recognizeed {text}")


            pass
    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue

        pass

def icao_input():
    print("hello world")
