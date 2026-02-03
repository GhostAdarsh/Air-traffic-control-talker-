import speech_recognition as sr
import pyttsx3
'''r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="en-GB")
    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Google error:", e)'''

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
def speak(text): 
    engine.say(text)
    engine.runAndWait()

speak("initialising JARVIS")
