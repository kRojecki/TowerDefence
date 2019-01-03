import pygame
from Game.Objects.Clickable import Clickable
from Game.Core.Handler.MouseHandler import MouseHandler


class Pointerable(Clickable):

    _position = ()
    _size = ()

    def __init__(self):
        MouseHandler.registerObject(self)

    def get_position(self):
        return self._position

    def get_size(self):
        return self._size
