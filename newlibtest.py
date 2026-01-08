import cv2 
import numpy as np 
import pygame 

pygame.init()
img = cv2.imread('LHRNEA.png')
screen = pygame.display.set_mode(1280, 800)
res = cv2.resize(img, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
running = True
while running: 
    for event in pygame.event.get():
        screen.blit(img, (0,0))
        

        if event.type == pygame.QUIT:
            running = False



