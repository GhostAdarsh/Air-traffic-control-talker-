import pygame 
import math 
from main import pathfinding



class Plane:
    def __init__(self, start_pos, path, image, speed=2):
        self.image = image
        self.rect = self.image.get_rect(center=start_pos)

        # convert everything to Vector2 once
        self.path = [pygame.Vector2(p) for p in path]
        self.current_node = 0

        self.speed = speed
        self.state = "FOLLOW"

        self.checkpoints = {5, 10}   # path indices
        self.waiting = False
        self.alive = True

    def update(self, takeoff_confirmed=False):
        if self.state == "FOLLOW":
            self.follow_astar_path()

        elif self.state == "WAIT":
            if takeoff_confirmed:
                self.state = "TAKEOFF"

        elif self.state == "TAKEOFF":
            self.takeoff()

    def follow_astar_path(self):
        if self.current_node >= len(self.path):
            self.state = "WAIT"
            return

        target = self.path[self.current_node]
        pos = pygame.Vector2(self.rect.center)

        direction = target - pos
        distance = direction.length()

        if distance <= self.speed:
            self.rect.center = target
            self.current_node += 1

            if self.current_node in self.checkpoints:
                self.state = "WAIT"
        else:
            direction.normalize_ip()
            pos += direction * self.speed
            self.rect.center = pos
