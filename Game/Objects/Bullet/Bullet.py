import pygame
from Game.Objects.Drawable import Drawable


class Bullet(Drawable):

    _position = (10, 10)
    _size = (2, 2)

    _target = 0
    _damage = 1
    _speed = 0.5

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.get_position(), self._size[0], 1)

    def update(self):
        self._position = (
            self._position[0] + self._speed,
            self._position[1]
        )
        pass
