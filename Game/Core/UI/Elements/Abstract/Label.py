import pygame

from Configuration.Configuration import Configuration
from Core.UI.Elements.Abstract.UIElement import UIElement
from Objects.Abstracts.Pointerable import Pointerable
from Utils.Constant import Color


class Label(UIElement, Pointerable):
    _font = None
    _font_color = Color.WHITE
    _prefix = ""

    _font_name = None

    def __init__(self, position, prefix, font_size=12):
        self._font_name = Configuration.get_str('DISPLAY', 'font.name')
        self._font = pygame.font.SysFont(self._font_name, font_size)
        self._position = position
        self._prefix = prefix

    def draw(self, screen):
        super().draw(screen)
        label = self._font.render(self._get_content_to_show(), False, self._font_color)
        screen.blit(label, self._position)

    def _get_content_to_show(self):
        return self._prefix

    def get_label_size(self):
        return self._font.size(self._get_content_to_show())

    def set_position(self, position):
        self._position = position
