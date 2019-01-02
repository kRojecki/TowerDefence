import pygame
from Game.Core import GameArea
from Utils.Constant import Position


class Tile:
    bitmap = 0
    _border_color = (90, 90, 90)
    _background_color = (10, 10, 10)
    _tile_position = [0, 0]
    _rect_position = ()

    def __init__(self, position):
        self._tile_position = position
        self._rect_position = self.calculate_position_and_size()

    # calculate position and size of field to draw
    def calculate_position_and_size(self):
        return ((self._tile_position[Position.Y] * GameArea.GameArea.field_size),
                (self._tile_position[Position.X] * GameArea.GameArea.field_size),
                GameArea.GameArea.field_size + 1, GameArea.GameArea.field_size + 1)

    def draw(self, screen):
        self.draw_border(screen)
        self.draw_tile_content(screen)

    def draw_border(self, screen):
        pygame.draw.rect(screen, self._border_color, self._rect_position, 1)

    def draw_tile_content(self, screen):
        inner_position = (self._rect_position[Position.X] + 1, self._rect_position[Position.Y] + 1, GameArea.GameArea.field_size - 1, GameArea.GameArea.field_size - 1)
        pygame.draw.rect(screen, self._background_color, inner_position, 0)

    def get_rect_position(self):
        return self._rect_position

    def get_tile_position(self):
        return self._tile_position
