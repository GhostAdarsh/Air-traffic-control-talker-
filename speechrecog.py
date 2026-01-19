print("hello world")
import pyttsx3 
import pyaudio
import speech_recognition as sr 
import os 




# getting the computer voice: 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#allowing compuiter to speak (?) 
print("initialising Air Talker")
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("hi")

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source: 
    recognizer.adjust_for_ambient_noise(source)
    print("Listening")

while True:
    with mic as source: 
        print("Listening")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google_cloud(audio)
        print("text")
        if "stop lsitening" in text.lower():
            print("stopping")
            break 
    except sr.UnknownValueError:
        print("repeat phrase")


