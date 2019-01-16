from Game.Objects.Enemy.Enemy import Enemy
import pygame
from Utils.Constant import Color, Position


class TriangleEnemy(Enemy):

    _size = (15, 15)
    _speed = 0.3
    _health = 75

    def draw(self, screen):
        cannon_points = [
            (self.get_position()[Position.X] + (self._size[Position.X] / 5), self.get_position()[Position.Y] + self._size[Position.Y] / 5),
            (self.get_position()[Position.X] + (4 * self._size[Position.X] / 5), self.get_position()[Position.Y] + (self._size[Position.Y]) / 2),
            (self.get_position()[Position.X] + (self._size[Position.X]) / 5, self.get_position()[Position.Y] + (4 * self._size[Position.Y]) / 5),
        ]
        pygame.draw.polygon(
            screen,
            Color.RED,
            cannon_points,
            2
        )
