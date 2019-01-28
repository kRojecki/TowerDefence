import uuid

import Game.Core.Event.Handler.MouseEventHandler
from Game.Utils.Constant import PointableState
from Objects.Abstracts.Clickable import Clickable


class Pointerable(Clickable):

    _position = ()
    _size = ()

    _layer = 0

    _state = PointableState.CLEAR

    _hash = ''

    def __init__(self):
        self._prepare_hash()
        Game.Core.Event.Handler.MouseEventHandler.MouseEventHandler.register_object(self, self._layer)

    def __del__(self):
        Game.Core.Event.Handler.MouseEventHandler.MouseEventHandler.unregister_object(self, self._layer)

    def get_position(self):
        return self._position

    def get_size(self):
        return self._size

    def _hover_action(self):
        self._state = PointableState.HOVER

    def _lost_focus_action(self):
        self._state = PointableState.CLEAR

    def _prepare_hash(self):
        self._hash = uuid.uuid1()

    def get_hash(self):
        return self._hash
