import pygame
from Game.Objects.Drawable import Drawable


class Enemy(Drawable):

    _position = (60, 60)
    _size = (5, 5)

    _health = 10
    _speed = 1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self._position, self._size[0], 1)

    def update(self):
        self._position = pygame.mouse.get_pos()
