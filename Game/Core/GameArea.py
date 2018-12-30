import pygame
import math
from Utils.Constant import Position
from Game.Objects.EmptyTile import EmptyTile
from pygame import Surface

class GameArea:

    screen = Surface((100,100))
    gameArea = []
    fieldSize = 50
    gameAreaMargin = [10, 10] # should be changed because of adding separated surface for gameArea
    gameAreaDimesions = [9,18]

    def __init__(self):
        self.screen = Surface((1000, 600))
        pass

    def initField(self):
        row = 0
        column = 0
        for areaRow in range(self.gameAreaDimesions[Position.X]):
            newRow = []
            for field in range(self.gameAreaDimesions[Position.Y]):
                newRow.append(EmptyTile([column, row]))
                row += 1
            column += 1
            row = 0
            self.gameArea.append(newRow)

    def update(self):
        self.screen.fill((5,5,5))
        selectedField = self.getSelectedField()
        self.drawFields(selectedField)
        return self.screen

    def changeField(self, position, newField):
        self.gameArea[position[Position.X]][position[Position.Y]] = newField

    # check if tile should be filled with color
    def shouldFill(self, field, position, selectedField):
        return 0 if field == 1 or (
                    selectedField[Position.X] == position[Position.X] and selectedField[Position.Y] == position[
                Position.Y]) else -1

    def drawFields(self, selectedField):
        for fieldRow in self.gameArea:
            for field in fieldRow:
                self.drawSingleField(field,selectedField)

    def drawSingleField(self, field, selectedField):
        selectionColor = (10, 10, 10, 10)

        field.draw(self.screen)

        if selectedField[Position.X] == field.position[Position.X] and selectedField[Position.Y] == field.position[Position.Y]:
            #pygame.draw.rect(self.screen, selectionColor, innerPosition, 0)
            pass

    # Rewrite and move calculate logic from here, after adding additional surface
    # Fails when gameAreaMargin or game surface will be changed
    def getSelectedField(self):
        mousePos = pygame.mouse.get_pos()

        x = math.floor((mousePos[Position.Y] - self.gameAreaMargin[Position.X]) / self.fieldSize)
        y = math.floor((mousePos[Position.X] - self.gameAreaMargin[Position.Y]) / self.fieldSize)

        # Protects from click outside of game area
        x = x if x <= self.gameAreaDimesions[Position.X] - 1 else -1
        y = y if y <= self.gameAreaDimesions[Position.Y] - 1 else -1

        if (x != -1 and y != -1 and pygame.mouse.get_pressed()[0] == 1):
             print(self.gameArea[x][y].position);

        return [x, y];
