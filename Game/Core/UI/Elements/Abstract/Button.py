import pygame

from Core.UI.Elements.Abstract.Label import Label
from Core.UI.Elements.Abstract.UIElement import UIElement
from Objects.Abstracts.Pointerable import Pointerable
from Utils.Constant import Color, PointableState, Position


class Button(UIElement, Pointerable):

    _size = (0, 0)
    _label = None

    _surface = None

    _background_color = {
        PointableState.CLEAR: Color.DARK_GRAY,
        PointableState.HOVER: Color.GRAY,
        PointableState.CLICKED: Color.LIGHT_GRAY,
        }

    _layer = 1

    _linked_element = None

    def __init__(self, content, position, linked_element):
        super().__init__()
        self._position = position
        self._surface = pygame.Surface(self._size, pygame.SRCALPHA)
        self._label = Label((0, 0), content, 14)
        self._label.set_position(self._calculate_label_position())
        self._linked_element = linked_element

    def draw(self, screen):
        super().draw(screen)
        self._surface.fill(self._get_background_color())
        self._label.draw(self._surface)
        screen.blit(self._surface, self._position)

    def _get_background_color(self):
        return self._background_color[self._state]

    def _calculate_label_position(self):
        label_size = self._label.get_label_size()
        surface_size = self.get_size()

        x = int((surface_size[Position.X] - label_size[Position.X])/2)
        y = int((surface_size[Position.Y] - label_size[Position.Y])/2)

        return (x, y)
