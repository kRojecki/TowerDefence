import sys
import pygame
from Game.Core.GameArea import GameArea

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

gameArea = GameArea()
gameArea.initField()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    screen.blit(gameArea.update(),(10,10))
    pygame.display.flip()