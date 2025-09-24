print("hello world") 

# import modules here: 
from PIL import Image
import tkinter as tk 
from matplotlib import image 
from matplotlib import pyplot as plt 
import pygame 
from pygame.locals import * 
pygame.init()


# set window dimensions 

window = pygame.display.set_mode((1000, 800))
bg_img = pygame.image.load.img("LondonHeathrowNEA.jpg")
bg = pygame.transform.scale(bg_img, (1000, 800))
i = 0 

run = True
while run: 
    window.fill(0,0,0)
    window.blit(bg_img, (0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()
pygame.quit()
        

        
        

pygame.display.update()
    



#image show function 

'''def startup(): # adds background and 2D grid 
        print("x")
        # background: 
        img = Image.open('LondonHeathrowNEA.jpg')
        desired_dpi = 500

        # plotting points on grid
        t5A = plt.plot(365, 390, marker='x', color="green")
        t5B = plt.plot(365, 445, marker='x', color="blue")
        t5C = plt.plot(400, 425, marker='x', color="red")
        t5D = plt.plot(435, 450, marker='x', color="purple")
        t5E = plt.plot(463, 407, marker='x', color="brown")
        t5F = plt.plot(493, 424, marker='x', color="magenta")

        t3A = plt.plot(610, 400, marker='x', color="black")
        t3B = plt.plot(635, 410, marker='x', color="cyan")
        t3C = plt.plot(649, 435, marker='x', color="red")

        t2A = plt.plot(785, 490, marker='x', color="black")
        t2B = plt.plot(815, 490, marker='x', color="red")

        runwayA = plt.plot(400, 300, marker='v', color='red')
        runwayB = plt.plot(900, 550, marker='v', color='red')
        
        plt.imshow(img)
        plt.show()

        # now i want to create the pathways using a class:
        class Pathways():
            def __init__(self):
                self.coordinates = None
                self.checkpoints = None
    #startup() '''





    

