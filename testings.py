# this isthe platform to "stage" tests: control c ad v 


# import modules here: 

import pygame 
from pygame import * 
import matplotlib 
from matplotlib import pyplot as plt 
from matplotlib import image 
#from objectplanes import Planes


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

# coordinate points - time consuming do this @ home 
#points = [(100, 100), (200, 200), (300, 300)]
# coordinate points - time consuming do this @ home (did this only for T5 PLANES)
points = [(360, 390), (360, 450), (490, 410), (407, 400), (429,400), (469, 450)]

# checkpoint coordinates - this is the junctions at the taxiway - takeoff and landing only  
checkpts = [(384, 358), (320,340), ]

landpts = [(300, 300), (400, 400)]


#create clock 
clock = pygame.time.Clock() 
clock = pygame.time.Clock()     









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

    for point in points: 
            pygame.draw.circle(screen, "red", point, 5)
    
    for checkpt in checkpts: 
            pygame.draw.circle(screen, "green", checkpt, 3)
        
    clock.tick(100)   
        
        






    pygame.display.update()


# TASK - create and plot coordinate on the 15 places on the background - set these as finishing points - DONE (lines  28 and 54 above)

