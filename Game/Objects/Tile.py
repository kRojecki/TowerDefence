import pygame
from Game.Core import GameArea
from Utils.Constant import Position


class Tile:
    bitmap = 0
    borderColor = (90, 90, 90)
    backgroundColor = (10, 10, 10)
    tilePosition = [0, 0]

    def __init__(self, position):
        self.position = position

    # calculate position and size of field to draw
    def calculatePositionAndSize(self, position):
        return ((position[Position.Y] * GameArea.GameArea.fieldSize),
                (position[Position.X] * GameArea.GameArea.fieldSize), GameArea.GameArea.fieldSize + 1, GameArea.GameArea.fieldSize + 1)

    def draw(self, screen):
        position = self.calculatePositionAndSize([self.position[Position.X], self.position[Position.Y]])
        pygame.draw.rect(screen, self.borderColor, position, 1)
        innerPosition = (position[Position.X] + 1, position[Position.Y] + 1, GameArea.GameArea.fieldSize - 1, GameArea.GameArea.fieldSize - 1)
        pygame.draw.rect(screen, self.backgroundColor, innerPosition, 0)
