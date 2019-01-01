from Game.Objects.Tile import Tile
import pygame
from Game.Core import GameArea
from Utils.Constant import Position
from pygame import Surface

class TurretTile(Tile):
    borderColor = (200, 90, 90)
    backgroundColor = (100, 10, 10)

    def drawTileContent(self, screen):
        innerPosition = (self.rectPosition[Position.X] + 1, self.rectPosition[Position.Y] + 1, GameArea.GameArea.fieldSize - 1, GameArea.GameArea.fieldSize - 1)
        innerPosition2 = (self.rectPosition[Position.X] + 2, self.rectPosition[Position.Y] + 2, GameArea.GameArea.fieldSize - 3, GameArea.GameArea.fieldSize - 3)
        pygame.draw.rect(screen, self.backgroundColor, innerPosition, 1)
        pygame.draw.rect(screen, self.borderColor, innerPosition2, 1)
        cannon = Surface((GameArea.GameArea.fieldSize, GameArea.GameArea.fieldSize),pygame.SRCALPHA)
        cannonRect = [
            (GameArea.GameArea.fieldSize/2, GameArea.GameArea.fieldSize/5),
            (GameArea.GameArea.fieldSize/5, (4*GameArea.GameArea.fieldSize)/5),
            ((4* GameArea.GameArea.fieldSize)/5, (4*GameArea.GameArea.fieldSize)/5),
        ]
        pygame.draw.polygon(cannon, self.borderColor, cannonRect, 1)
        cannon
        screen.blit(cannon,(self.rectPosition[Position.X], self.rectPosition[Position.Y]))
