#OOP class planes 
import pygame 
import random 
import math 
#from main import Pathfinder 
pygame.init()
print("helloworld")
# prerequisites 
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('triple7.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
images = [ 
     "myFavplane.png", 
     "the320.png", 
     "the350.png",
     "TheMonarchy .png", 
     "triple7.png"
     ]
random_img = random.choice(images)

