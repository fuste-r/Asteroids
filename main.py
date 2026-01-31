import pygame
from constants import *
from logger import log_state
from player import *

def main():
    #init vars
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt =0
    player_x =  SCREEN_WIDTH/2
    player_y = SCREEN_HEIGHT/2
    p1 = Player(player_x, player_y)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # begin game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        p1.update(dt)

        screen.fill("black")
        
        p1.draw(screen)
        pygame.display.flip()
        clock.tick(60)    
        dt = (clock.tick(60))


    
if __name__ == "__main__":
    main()
