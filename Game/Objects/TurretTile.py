from Game.Objects.Tile import Tile
import pygame
from Game.Core import GameArea
from Utils.Constant import Position
from pygame import Surface
from pygame import Rect

class TurretTile(Tile):
    borderColor = (200, 90, 90)
    backgroundColor = (100, 10, 10)
    cannonRectOriginal = ()
    rotation = 0;

    def drawTileContent(self, screen):
        innerPosition = (self.rectPosition[Position.X] + 1, self.rectPosition[Position.Y] + 1, GameArea.GameArea.fieldSize - 1, GameArea.GameArea.fieldSize - 1)
        innerPosition2 = (self.rectPosition[Position.X] + 2, self.rectPosition[Position.Y] + 2, GameArea.GameArea.fieldSize - 3, GameArea.GameArea.fieldSize - 3)
        pygame.draw.rect(screen, self.backgroundColor, innerPosition, 1)
        pygame.draw.rect(screen, self.borderColor, innerPosition2, 1)
        self.cannonRectOriginal = (GameArea.GameArea.fieldSize, GameArea.GameArea.fieldSize)
        cannon = Surface(self.cannonRectOriginal,pygame.SRCALPHA)
        cannonRect = [
            ((GameArea.GameArea.fieldSize/2), GameArea.GameArea.fieldSize/5),
            (GameArea.GameArea.fieldSize/5, (4*GameArea.GameArea.fieldSize)/5),
            ((4* GameArea.GameArea.fieldSize)/5, (4*GameArea.GameArea.fieldSize)/5),
        ]
        pygame.draw.polygon(cannon, self.borderColor, cannonRect, 1)
        cannon = pygame.transform.rotate(cannon,self.rotation)

        positionModifier = (0,0)
        cannonRectNew = cannon.get_rect();

        positionModifier = ((self.cannonRectOriginal[0] - cannonRectNew.width)/2, (self.cannonRectOriginal[1] - cannonRectNew.height)/2)
        print(positionModifier)
        print(self.rectPosition[Position.X]-positionModifier[Position.X], self.rectPosition[Position.Y]-positionModifier[Position.Y])

        blitDest = (self.rectPosition[Position.X]+positionModifier[Position.X], self.rectPosition[Position.Y]+positionModifier[Position.Y])
        screen.blit(cannon, blitDest)
        
        self.rotation += 1;
        print(cannon.get_rect())