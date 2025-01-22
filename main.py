# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroidField = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            a.update(dt)
            if a.collide(player):
                print("Game Over!")
                sys.exit()
            for s in shots:
                if a.collide(s):
                    a.split()
                    s.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
