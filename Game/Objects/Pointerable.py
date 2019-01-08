from Game.Objects.Clickable import Clickable
from Game.Core.Event.Handler.MouseHandler import MouseHandler
from Game.Utils.Constant import PointableState


class Pointerable(Clickable):

    _position = ()
    _size = ()

    _state = PointableState.CLEAR

    def __init__(self):
        MouseHandler.register_object(self)

    def get_position(self):
        return self._position

    def get_size(self):
        return self._size

    def _hover_action(self):
        self._state = PointableState.HOVER

    def _lost_focus_action(self):
        self._state = PointableState.CLEAR
