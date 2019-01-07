import pygame
from Game.Utils.Constant import Color, Position, PointableState, EventEnum
from Game.Objects.Pointerable import Pointerable
from Game.Objects.Centerable import Centerable


class Tile(Pointerable, Centerable):
    bitmap = 0
    _border_color = Color.GRAY
    _background_color = {
        PointableState.CLEAR: Color.DARK_GRAY,
        PointableState.HOVER: Color.GRAY,
        PointableState.CLICKED: Color.WHITE
        }
    _tile_position = [0, 0]

    _state = PointableState.CLEAR

    def __init__(self, position, size, game_area_margin):
        super().__init__()
        self._tile_position = position
        self._size = (size, size)
        self._position = self.calculate_position_and_size()

    # calculate position and size of field to draw
    def calculate_position_and_size(self):
        return ((self._tile_position[Position.Y] * self._size[Position.Y]),
                (self._tile_position[Position.X] * self._size[Position.X]))

    def draw(self, screen):
        self._draw_border(screen)
        self._draw_tile_content(screen)

    def update(self, nearest_enemy_position):
        pass

    def _draw_border(self, screen):
        pygame.draw.rect(screen, self._border_color, (self._position, self._size), 1)

    def _draw_tile_content(self, screen):
        inner_position = (self._position[Position.X] + 1, self._position[Position.Y] + 1, self._size[Position.X] - 1, self._size[
            Position.Y] - 1)
        pygame.draw.rect(screen, self._get_background_color(), inner_position, 0)

    def _get_background_color(self):
        return self._background_color[self._state]

    def get_tile_position(self):
        return self._tile_position

    def get_size(self):
        return self._size

    def _hover_action(self):
        self._state = PointableState.HOVER

    def _lost_focus_action(self):
        self._state = PointableState.CLEAR

    def _click_action(self, button):
        pygame.event.post(
            pygame.event.Event(
                EventEnum.TILE_CLICKED,
                {
                    "tile": self,
                    "button": button
                }
            )
        )
