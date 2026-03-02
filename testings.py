
import pygame 
import math
import matplotlib 
from matplotlib import pyplot as plt 
from matplotlib import image 
import pathfinding 
from pathfinding.core.grid import Grid  
from pathfinding.finder.a_star import AStarFinder 
from pathfinding.core.diagonal_movement import DiagonalMovement
import random

pts = [(45,48),(45,56),(61,51),(55,50),(53,56),(50,50)]
fpts = [(41,38), (68, 43)]
# coordinate points - time consuming do this @ home (did this only for T5 PLANES)
apronpts = [(360, 390), (360, 450), (490, 410), (407, 400), (429,400), (469, 450)]
# checkpoint coordinates - this is the junctions at the taxiway - takeoff and landing only  
checkpts = [(384, 358), (320,340), ]
landpts = [(300, 300), (400, 400)]

CELL_SIZE = 8

class Pathfinder:
    def __init__(self, matrix, screen):
        self.matrix = matrix
        self.screen = screen
        self.grid = Grid(matrix=matrix)

        self.select_surf = pygame.image.load('crosshairX.png').convert_alpha()
        self.actual_image = pygame.transform.scale(self.select_surf, (CELL_SIZE, CELL_SIZE))

        self.path = []

    def create_path(self):
        # reset grid each time (IMPORTANT for pathfinding library)
        self.grid = Grid(matrix=self.matrix)

        # random start
        start_x, start_y = random.choice(pts)
        start = self.grid.node(start_x, start_y)

        # fixed end point
        end_x, end_y = (38, 40)
        end = self.grid.node(end_x, end_y)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        self.path, _ = finder.find_path(start, end, self.grid)

        print([(node.x, node.y) for node in self.path])

    def draw_path(self):
        if len(self.path) > 1:
            points = [
                (
                    node.x * CELL_SIZE + CELL_SIZE // 2,
                    node.y * CELL_SIZE + CELL_SIZE // 2
                )
                for node in self.path
            ]

            pygame.draw.lines(self.screen, (255, 0, 0), False, points, 3)

    def draw_active_cell(self):
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // CELL_SIZE
        col = mouse_pos[0] // CELL_SIZE

        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.actual_image, rect)

pathfinder = Pathfinder(matrix, screen)
