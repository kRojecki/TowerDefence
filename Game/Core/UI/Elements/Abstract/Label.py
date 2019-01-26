import pygame

from Core.Event.Handler.MouseHandler import MouseHandler
from Core.UI.Elements.Abstract.UIElement import UIElement
from Objects.Abstracts.Pointerable import Pointerable
from Utils.Constant import Color


class Label(UIElement, Pointerable):
    _font = None
    _font_color = Color.WHITE
    _prefix = ""

    _font_name = "ubuntumono"

    def __init__(self, prefix, position, font_size=16):
        self._font = pygame.font.SysFont(self._font_name, font_size)
        self._position = position
        self._prefix = prefix

    def draw(self, screen):
        super().draw(screen)
        label = self._font.render(self._get_content_to_show(), 1, self._font_color)
        screen.blit(label, self._position)

    def _get_content_to_show(self):
        return self._prefix

    def _click_action(self, pressed):
        print('Button pressed!')
