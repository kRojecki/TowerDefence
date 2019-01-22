import pygame

from Core.UI.Elements.Abstract.UIElement import UIElement
from Utils.Constant import Color


class Label(UIElement):
    _font = None
    _font_color = Color.WHITE
    _prefix = ""
    _value = 0

    _font_name = "ubuntumono"
    _font_size = 16

    def __init__(self):
        self._font = pygame.font.SysFont(self._font_name, self._font_size)

    def draw(self, screen):
        label = self._font.render(self._prefix + str(self._value), 1, self._font_color)
        screen.blit(label, self._position)
