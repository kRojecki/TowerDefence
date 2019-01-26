import pygame
from pygame.rect import Rect

from Core.UI.Elements.Abstract.UIElement import UIElement
from Utils.Constant import Color


class Panel(UIElement):

    _size = (100, 100)
    _linked_element = None
    _surface = None

    _elements = []

    def __init__(self, linked_element):
        self._linked_element = linked_element
        self._position = linked_element.get_center()
        self._surface = pygame.Surface(self._size)

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.rect(self._surface, Color.GRAY, Rect((0, 0), self._size), 1)
        for element in self._elements:
            element.draw(self._surface)
        screen.blit(self._surface, self._position)
