from Game.Objects.Tile.Tile import Tile
import pygame
from Utils.Constant import Position
from pygame import Surface

from Utils.Helper.TransformHelper.RotationHelper import RotationHelper


class TurretTile(Tile):
    _border_color = (200, 90, 90)
    _background_color = (100, 10, 10)
    _rotation = 0

    def _draw_border(self, screen):
        super()._draw_border(screen)
        second_border_rect = (self._position[Position.X] + 2, self._position[Position.Y] + 2,
                              self._size[Position.X] - 3, self._size[Position.Y] - 3)

        pygame.draw.rect(screen, self._border_color, second_border_rect, 1)

    def _draw_tile_content(self, screen):
        super()._draw_tile_content(screen)
        cannon = self.draw_cannon()
        rotation_dto = RotationHelper.rotate(cannon, self._rotation)

        blit_destination = (self._position[Position.X] - rotation_dto.position_modifier[Position.X],
                            self._position[Position.Y] - rotation_dto.position_modifier[Position.Y])
        screen.blit(rotation_dto.transformed_surface, blit_destination)

        self._rotation = (self._rotation + 1) % 360

    def draw_cannon(self):
        cannon = Surface(self._size, pygame.SRCALPHA)
        cannon_points = [
            ((self._size[Position.X] / 2), self._size[Position.Y] / 10),
            (self._size[Position.X] / 5, (3.5 * self._size[Position.Y]) / 5),
            ((4 * self._size[Position.X]) / 5, (3.5 * self._size[Position.Y]) / 5),
        ]

        pygame.draw.polygon(cannon, self._border_color, cannon_points, 0)

        return cannon
