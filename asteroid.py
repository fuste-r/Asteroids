from circleshape import CircleShape
import pygame
from constants import *
import sys
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position+= (self.velocity* dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new1 = Asteroid(self.position[0], self.position[1], self.radius/2)
            new2 = Asteroid(self.position[0], self.position[1], self.radius/2)
            new1.velocity = pygame.math.Vector2.rotate(self.velocity, angle)
            new2.velocity = pygame.math.Vector2.rotate(self.velocity, (angle * -1))
