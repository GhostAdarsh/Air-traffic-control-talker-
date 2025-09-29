# import modules and objects here: 
import pygame 
from pygame import * 
import matplotlib 
from matplotlib import pyplot as plt 
from matplotlib import image 
from objectplanes import Planes


print("X")

# TASK A - load an image and setr it as background - DONE

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

# coordinate points - time consuming do this @ home (did this only for T5 PLANES)
points = [(360, 390), (360, 450), (490, 410), (407, 400), (429,400), (469, 450)]
# checkpoint coordinates - this is the junctions at the taxiway - takeoff and landing only  
checkpts = [(384, 358), (320,340), ]
landpts = [(300, 300), (400, 400)]


#create clock 
clock = pygame.time.Clock()     








# while loop to keep code running 
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

    # draws the coordinate pts 
    for point in points: 
            pygame.draw.circle(screen, "red", point, 5)
    for checkpt in checkpts: 
            pygame.draw.circle(screen, "green", checkpt, 3)
    for landpt in landpts:
            pygame.draw.circle(screen, "blue", landpt, 3)
        
    clock.tick(100)   
        
        






    pygame.display.update()


# TASK  B - create and plot coordinate on the 15 places on the background - set these as finishing points - DONE (lines  28 and 54 above)

# TASK C - create object (planes) - set image to them and make them follow a path - diffictult - use OOP 
# split task c to 2 pts 
# watch pathfinding algorithm found on yt - work on that eg 
a = Planes("BA277")
b = Planes("BA776")
c = Planes("BA928")
d = Planes("")     
e = Planes("")

departures = [a, b, c, d, e]

for departure in departures():
      print("X")



pygame.quit() 
