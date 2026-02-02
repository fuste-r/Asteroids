import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroidfield import *
from asteroid import *
from shot import *

def main():
    #init vars
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt =0
    player_x =  SCREEN_WIDTH/2
    player_y = SCREEN_HEIGHT/2

    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    
    p1 = Player(player_x, player_y)
    a1 = AsteroidField()
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
        for a in asteroids:
            if a.collides_with(p1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for items in drawable:
            items.draw(screen)
                
        pygame.display.flip()
        dt = (clock.tick(60)/1000)


    
if __name__ == "__main__":
    main()
