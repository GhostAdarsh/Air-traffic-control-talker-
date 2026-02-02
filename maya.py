import speech_recognition as sr 
import pyttsx3
import pygame
import pyaudio 
import google 
import smtplib
import os
import datetime
import wikipedia
import boto3 
from gtts import gTTS
from playsound import playsound

polly = boto3.client(
    "polly", 
    region_name = "eu-west-2"    
)
pygame.init() 
r = sr.Recognizer()


screen = pygame.display.set_mode((1280,800)) # edited the image width nd height for easier thingyies    
#add background
background = pygame.image.load("LondonHeathrowNEA.jpg")
pygame.transform.scale(background, (50,50))
clock = pygame.time.Clock() 


# add engine voice 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
for voice in voices: 
    if 'David' in voice.name: 
        engine.setProperty('voice', voice.id)

def speak(text): 
    engine.say(text)
    engine.runAndWait()


class Planes: 

    def __init__(self):
        print("X")
        
        

    def record_Audio(): 
        print("x")
        speak("recording audio")
        with sr.Microphone() as mic: 

            r.adjust_for_ambient_noise(mic, duration = 0.2)
            audio = r.listen(mic)

            text = r.recognize_amazon(audio)
            text = text.lower() 

            print(f"Recognised {text}")

running = True 
while running: 
    #colour scheme 
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    

    #speechrecog
    
        
    for event in pygame.event.get():
        # if tab key pressed, quits game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pygame.quit()
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Planes.record_Audio()


    pygame.display.update() 

    clock.tick(100)


