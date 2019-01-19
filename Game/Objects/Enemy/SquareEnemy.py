from Game.Objects.Enemy.Enemy import Enemy
import pygame
from Utils.Constant import Color, Position


class SquareEnemy(Enemy):

    _size = (15, 15)
    _speed = 0.15
    _max_health = 200
    _rotation = 0

    _rotated = False

    def draw(self, screen):

        super().draw(screen)
        rect = pygame.Rect(
            0,
            0,
            self.get_size()[Position.X] - int(self._border_width/2),
            self.get_size()[Position.Y] - int(self._border_width/2),
        )
        pygame.draw.rect(self._surface, Color.RED, rect, self._border_width)
        self.blit(screen)

    def update(self):
        super().update()
        if self._rotated:
            self._rotation = (self._rotation + 1 % 90)
