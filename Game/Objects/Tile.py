import pygame
from Game.Core import GameArea
from Utils.Constant import Position


class Tile:
    bitmap = 0
    borderColor = (90, 90, 90)
    backgroundColor = (10, 10, 10)
    tilePosition = [0, 0]
    rectPosition = ()

    def __init__(self, position):
        self.tilePosition = position
        self.rectPosition = self.calculatePositionAndSize()

    # calculate position and size of field to draw
    def calculatePositionAndSize(self):
        return ((self.tilePosition[Position.Y] * GameArea.GameArea.fieldSize),
                (self.tilePosition[Position.X] * GameArea.GameArea.fieldSize), GameArea.GameArea.fieldSize + 1, GameArea.GameArea.fieldSize + 1)

    def draw(self, screen):
        self.__drawBorder(screen)
        self.drawTileContent(screen)

    def __drawBorder(self, screen):
        pygame.draw.rect(screen, self.borderColor, self.rectPosition, 1)

    def drawTileContent(self, screen):
        innerPosition = (self.rectPosition[Position.X] + 1, self.rectPosition[Position.Y] + 1, GameArea.GameArea.fieldSize - 1, GameArea.GameArea.fieldSize - 1)
        pygame.draw.rect(screen, self.backgroundColor, innerPosition, 0)
