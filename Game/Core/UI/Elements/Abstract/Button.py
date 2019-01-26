import pygame

from Core.UI.Elements.Abstract.Label import Label
from Core.UI.Elements.Abstract.UIElement import UIElement
from Objects.Abstracts.Pointerable import Pointerable
from Utils.Constant import Color
from Utils.Helper.DataSetHelper.TupleTransformer import TupleTransformer


class Button(UIElement, Pointerable):

    _size = (80, 20)
    _label = None

    _surface = None

    _layer = 1

    def __init__(self, content, position):
        super().__init__()
        self._position = position
        self._label = Label(content, (4, 4), 14)
        self._surface = pygame.Surface(TupleTransformer.add_to_tuple(self._size, 2), pygame.SRCALPHA)

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.rect(self._surface, Color.GRAY, pygame.Rect(self._position, self._size), 1)
        self._label.draw(self._surface)
        screen.blit(self._surface, self._position)

    def _hover_action(self):
        print('hover!!')
