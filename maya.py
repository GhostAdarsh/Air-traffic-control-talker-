import speech_recognition as sr 
import pyttsx3
import pygame
import pyaudio 
import google 
import smtplib
pygame.init() 
r = sr.Recognizer()

screen = pygame.display.set_mode((1280,800)) # edited the image width nd height for easier thingyies    
#add background
background = pygame.image.load("LondonHeathrowNEA.jpg")


class Planes: 

    def __init__(self):
        print("X")
        
        

    def record_Audio(): 
        print("x")
        with sr.Microphone() as mic: 

            r.adjust_for_ambient_noise(mic, duration = 0.2)
            audio = r.listen(mic)

            text = r.recognize_google_cloud(audio)
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
