import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create the image (or load one)
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))

        # Get rectangle
        self.rect = self.image.get_rect()

        # Random spawn position
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def update(self):
        pass  # movement logic here if needed
