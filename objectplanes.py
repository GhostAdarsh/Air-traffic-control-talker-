
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
          


pygame.init() 

# TASK A - load an image and setr it as background - DONE
#create screen
screen = pygame.display.set_mode((1280,800)) # edited the image width nd height for easier thingyies    
#add background
background = pygame.image.load("LondonHeathrowNEA.jpg")
#background = pygame.transform.scale(background, (col, row))
#scale background 
pygame.transform.scale(background, (50, 50))
# set icon 
win_icon = pygame.image.load("flightradar24.jfif")
pygame.display.set_icon(win_icon)
#set window title 
pygame.display.set_caption("Air Traffic Talker")

plane = Planes() 

running = True
while running: 
    
    #colour scheme 
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))

    # once mouse / tab key / everything pressed 
    for event in pygame.event.get():
    
        # if tab key pressed, quits game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pygame.quit()
        if event.type == pygame.QUIT: 
            running = False
        if keys[pygame.MOUSEBUTTONDOWN]:
            plane.__init__()
            
            