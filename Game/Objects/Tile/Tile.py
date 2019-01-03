import pygame
from Utils.Constant import Position
from Utils.Constant import Color
from Game.Objects.Pointerable import Pointerable


class Tile(Pointerable):
    bitmap = 0
    _border_color = Color.GRAY
    _background_color = Color.DARK_GRAY
    _tile_position = [0, 0]

    def __init__(self, position, size, game_area_margin):
        super().__init__()
        self._tile_position = position
        self._size = (size, size)
        self._position = self.calculate_position_and_size(game_area_margin)

    # calculate position and size of field to draw
    def calculate_position_and_size(self, game_area_margin):
        return ((self._tile_position[Position.Y] * self._size[Position.Y]),
                (self._tile_position[Position.X] * self._size[Position.X]))

    def draw(self, screen):
        self._draw_border(screen)
        self._draw_tile_content(screen)

    def _draw_border(self, screen):
        pygame.draw.rect(screen, self._border_color, (self._position, self._size), 1)

    def _draw_tile_content(self, screen):
        inner_position = (self._position[Position.X] + 1, self._position[Position.Y] + 1, self._size[Position.X] - 1, self._size[Position.Y] - 1)
        pygame.draw.rect(screen, self._background_color, inner_position, 0)

    def get_tile_position(self):
        return self._tile_position

    def _hover_action(self):
        self._background_color = Color.LIGHT_GRAY

    def _click_action(self, button):

        # handle left button
        if button[0] == 1:
            self._background_color = Color.RED

        # handle right button
        if button[2] == 1:
            self._background_color = Color.GRAY

        print('Clicked', self.get_tile_position())
