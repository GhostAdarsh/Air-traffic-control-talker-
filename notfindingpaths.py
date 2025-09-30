import pygame, sys 
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


class Pathfinder:
    def __init__(self, matrix):

        # setup 
        self.matrix = matrix 
        self.grid = Grid(matrix = matrix)
        self.select_surf = pygame.image.load('LHRNEA.png').convert_alpha()

    def draw_active_cell(self):
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        #row = mouse_pos[1] // 32 
        #col = mouse_pos[0] // 32 
        #rect = pygame.Rect((col * 32,row * 32), (32,32))
        #screen.blit(self.select_surf, rect)



    def update(self):
        self.draw_active_cell()


# pygame etup 
pygame.init()
screen = pygame.display.set_mode((1280,736))
clock = pygame.time.Clock()


# game set 
bg_surf = pygame.image.load("LHRNEA.png").convert()


matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
]
pathfinder = Pathfinder(matrix)
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surf, (0,0))
    pathfinder.draw_active_cell()

    pygame.display.update()
    clock.tick(60)
    


print("s")
