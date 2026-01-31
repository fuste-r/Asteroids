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
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
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
        updatable.update(dt)

        screen.fill("black")
        for items in drawable:
            items.draw(screen)        
        pygame.display.flip()
        clock.tick(60)    
        dt = (clock.tick(60))


    
if __name__ == "__main__":
    main()
