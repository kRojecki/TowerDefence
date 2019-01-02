from Game.Objects.Tile import Tile
import pygame
from Game.Core import GameArea
from Utils.Constant import Position
from pygame import Surface

from Utils.Helper.TransformHelper.RotationHelper import RotationHelper


class TurretTile(Tile):
    _border_color = (200, 90, 90)
    _background_color = (100, 10, 10)
    _rotation = 0

    def draw_border(self, screen):
        super().draw_border(screen)
        second_border_rect = (self._rect_position[Position.X] + 2, self._rect_position[Position.Y] + 2,
                              GameArea.GameArea.field_size - 3, GameArea.GameArea.field_size - 3)

        pygame.draw.rect(screen, self._border_color, second_border_rect, 1)

    def draw_tile_content(self, screen):
        super().draw_tile_content(screen)
        cannon = self.draw_cannon()
        rotation_dto = RotationHelper.rotate(cannon, self._rotation)

        blit_destination = (self._rect_position[Position.X] - rotation_dto.position_modifier[Position.X],
                            self._rect_position[Position.Y] - rotation_dto.position_modifier[Position.Y])
        screen.blit(rotation_dto.transformed_surface, blit_destination)

        self._rotation = (self._rotation + 1) % 360

    def draw_cannon(self):
        cannon = Surface((GameArea.GameArea.field_size, GameArea.GameArea.field_size), pygame.SRCALPHA)
        cannon_points = [
            ((GameArea.GameArea.field_size / 2), GameArea.GameArea.field_size / 10),
            (GameArea.GameArea.field_size / 5, (3.5 * GameArea.GameArea.field_size) / 5),
            ((4 * GameArea.GameArea.field_size) / 5, (3.5 * GameArea.GameArea.field_size) / 5),
        ]

        pygame.draw.polygon(cannon, self._border_color, cannon_points, 0)

        return cannon
