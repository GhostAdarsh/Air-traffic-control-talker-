import cv2 
import numpy as np 
import pygame 

pygame.init()
img = cv2.imread('LHRNEA.png')
res = cv2.resize(img, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
running = True
while running: 
    for events in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


