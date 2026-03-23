## final testing of the planefucntion: 
import pygame 
from main import Plane 
TILE_SIZE = 8 

pygame.init() 
screen = pygame.display.set_mode(800, 600)
plane = Plane((0,0), "speedbird123")
assert plane.callsign == "speedbird123"
assert plane.grid_position == (2,3)
assert plane.index == 0 
assert plane.finished == False 
assert plane.speed == 0.2    
print("contructor test passed")
try: 
        Plane("wrong", "BA123")
        assert False  # shoudnt reach here 
except ValueError: 
        print("invalid start pos passed")
path = [(0,0), (0,1), (0,2)]
plane.set_path(path)
assert plane.path == path 
assert plane.index == 0 
assert plane.finished == False 
print("test plane movement update passed")
plane.set_path([0,0]) # single node - nothing to move 
plane.update() 
assert plane.finished == True 
print("test update finish passed")



 
