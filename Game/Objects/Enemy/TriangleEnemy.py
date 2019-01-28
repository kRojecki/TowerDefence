import pygame

from Game.Objects.Enemy.Enemy import Enemy
from Utils.Constant import Color, Position


class TriangleEnemy(Enemy):

    _size = (15, 15)
    _speed = 4
    _max_health = 75

    def draw(self, screen):
        super().draw(screen)
        self._set_rotation_by_move_direction()
        cannon_points = [
            ((self._size[Position.X] / 5), self._size[Position.Y] / 5),
            ((4 * self._size[Position.X] / 5), (self._size[Position.Y]) / 2),
            ((self._size[Position.X]) / 5, (4 * self._size[Position.Y]) / 5),
        ]
        pygame.draw.polygon(
            self._surface,
            Color.RED,
            cannon_points,
            self._border_width
        )

        self.blit(screen)

    def _set_rotation_by_move_direction(self):
        if self._move_vector == (0, 1):
            self._rotation = -90
        if self._move_vector == (0, -1):
            self._rotation = 90
        if self._move_vector == (1, 0):
            self._rotation = 0
        if self._move_vector == (-1, 0):
            self._rotation = 180
