# import modules here: 
import pygame 
from pygame import * 
import matplotlib 
from matplotlib import pyplot as plt 
from matplotlib import image 


print("X")

# TASK - load an image and setr it as background - DONE

#create screen
screen = pygame.display.set_mode((1250,800))

#add background
background = pygame.image.load("LondonHeathrowNEA.jpg")

#scale background 
pygame.transform.scale(background, (50, 50))
# set icon 
win_icon = pygame.image.load("flightradar24.jfif")
pygame.display.set_icon(win_icon)

#set window title 
pygame.display.set_caption("Air Traffic Talker")

running = True
while running: 
    #colour scheme 
    screen.fill((0,0,0))
    
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        # if tab key pressed, quits game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pygame.quit()
        if event.type == pygame.QUIT: 
            running = False
    pygame.display.update()


# TASK - create and plot coordinate on the 15 places on the background - set these as finishing points 

#pygame.draw.circle(surface, color, center, radius, width)



pygame.quit() 
