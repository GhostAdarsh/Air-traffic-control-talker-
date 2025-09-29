print("hello") 
# apply pygame to pathfinding (still watching yt vid)
import pygame, sys 
import pathfinding 

pygame.init()
screen = pygame.display.set_mode((1280 , 736))
clock = pygame.time.Clock() 


# game ssetup 
bg_surf = pygame.image.load("LHRNEA.png").convert()
bg_surf = pygame.transform.scale()
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # reused tab key bcs cba to click x on a window
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pygame.quit()
    screen.blit(bg_surf, (0,0))
    


    pygame.display.update()
    clock.tick(60)
