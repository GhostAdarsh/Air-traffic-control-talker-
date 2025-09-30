import pygame, sys 
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement



class Pathfinder:
    def __init__(self, matrix):

        # setup 
        self.matrix = matrix 
        self.grid = Grid(matrix = matrix)
        self.select_surf = pygame.image.load('crosshairX.png').convert_alpha()

        # pathfinding 
        self.path = []


    def draw_active_cell(self):
        # the mouse part isnt needed in the main.py code 
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        row = mouse_pos[1] // 32 
        col = mouse_pos[0] // 32 
        current_cell_value = self.matrix[row][col]
        if current_cell_value == 0:
            rect = pygame.Rect((col * 32,row * 32), (32,32))
            screen.blit(self.select_surf, rect)

    def create_path(self):
        # start pt 
        start_x, start_y =  [1,1]
        start = self.grid.node(start_x, start_y)

        #end pt 
        mouse_pos = pygame.mouse.get_pos()
        end_x, end_y = mouse_pos[0] // 32, mouse_pos[1] // 32
        end = self.grid.node(end_x, end_y)


         
        # path 
        finder = AStarFinder(diagonal_movement =  DiagonalMovement.always)
        self.path = finder.find_path(start, end, self.grid)
        print(self.path)




    


    def update(self):
        self.draw_active_cell()
        self.create_path()


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
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0,],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0,],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0,],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,],
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
