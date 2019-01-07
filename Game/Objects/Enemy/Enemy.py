import pygame
from Game.Objects.Centerable import Centerable

class Enemy(Centerable):

    _position = (60, 60)
    _size = (5,5)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self._position, self._size[0], 1)

    def get_position(self):
        return self._position

    def update(self):
        self._position = pygame.mouse.get_pos()
