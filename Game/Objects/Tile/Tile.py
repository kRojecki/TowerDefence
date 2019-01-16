import pygame
from Game.Utils.Constant import Color, Position, PointableState, EventEnum
from Objects.Interfaces.Pointerable import Pointerable
from Objects.Interfaces.Drawable import Drawable
from Objects.Interfaces.Changeable import Changeable
from Game.Core.Calculator.Tile.TilePositionCalculator import TilePositionCalculator
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher


class Tile(Pointerable, Drawable, Changeable):

    _border_color = Color.GRAY

    _background_color = {
        PointableState.CLEAR: Color.DARK_GRAY,
        PointableState.HOVER: Color.GRAY,
        PointableState.CLICKED: Color.WHITE
        }

    _tile_position = [0, 0]

    def __init__(self, position, size):
        super().__init__()
        self._tile_position = position
        self._size = (size, size)
        self._position = TilePositionCalculator.calculate_position(self)

    def draw(self, screen):
        self._draw_border(screen)
        self._draw_tile_content(screen)

    def update(self, nearest_enemy_position):
        pass

    def get_tile_position(self):
        return (
            self._tile_position[Position.Y],
            self._tile_position[Position.X]
        )
        # change coordinates because of array

    def get_size(self):
        return self._size

    def _draw_border(self, screen):
        pygame.draw.rect(screen, self._border_color, (self._position, self._size), 1)

    def _draw_tile_content(self, screen):
        inner_position = (
            self._position[Position.X] + 1, self._position[Position.Y] + 1,
            self._size[Position.X] - 1, self._size[Position.Y] - 1
        )
        pygame.draw.rect(screen, self._get_background_color(), inner_position, 0)

    def _get_background_color(self):
        return self._background_color[self._state]

    def _click_action(self, button):
        EventDispatcher.dispatch(
            EventEnum.TILE_CLICKED,
            {
                "tile": self,
                "button": button
            }
        )
