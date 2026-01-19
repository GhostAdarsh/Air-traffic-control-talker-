#OOP class planes 
import pygame 
import random 
#from main import Pathfinder 

print("helloworld")
images = [ 
     "myFavplane.png", 
     "the320.png", 
     "the350.png",
     "TheMonarchy .png", 
     "triple7.png"
     ]
random_img = random.choice(images)
class Planes(pygame.sprite.Sprite):
     print("X")
     def __init__(self):
          super().__init__()
          self.image = pygame.image.load(random_img).convert_alpha()
          self.rect = self.image.get.rect(center =  (45,48))








          
          self.flight_code = None 
          self.path = None 
          self.image = None 
          print(self.image)
          




