#module import 
import pygame 
import pathfinding 
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


# inital setup s

screen = pygame.display.set_mode((1280, 800))
background = pygame.image.load("LondonHeathrowNEA.jpg")
pygame.transform.scale(background, (50,50))
win_icon = pygame.image.load("flightradar24.jfif")
pygame.display.set_icon(win_icon)
pygame.display.set_caption("Air Traffic Talker")

clock = pygame.time.Clock() 


running = True
while running: 
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pygame.quit()
        if event.type == pygame.QUIT:
            running = False


