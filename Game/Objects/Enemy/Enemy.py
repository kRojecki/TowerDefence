from Game.Objects.Drawable import Drawable
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant import EventEnum, Color
from Objects.Pathable import Pathable
from Utils.Constant import Position
from Utils.Helper.TransformHelper.RotationHelper import RotationHelper


class Enemy(Drawable, Pathable):

    ALIVE = 0
    KILLED = 1

    _position = (60, 60)
    _size = (5, 5)

    _health = 100
    _speed = 0.25

    _rotation = 0

    _state = ALIVE

    def __init__(self, start_position, path):
        self._position = start_position
        self._path = path

    def draw(self, screen):
        if self._state != self.ALIVE:
            return

    def update(self):

        move_vector = self._get_move_vector()

        if self._state == self.ALIVE:
            self._position = (
                self._position[Position.X] + (move_vector[Position.X] * self._speed),
                self._position[Position.Y] + (move_vector[Position.Y] * self._speed)
            )

    def hit(self, damage):
        self._health = self._health - damage
        if self._health <= 0:
            self._death()

    def _death(self):
        EventDispatcher.dispatch(
            EventEnum.ENEMY_KILLED,
            {
                'enemy': self,
            }
        )
        self._state = self.KILLED

    def get_state(self):
        return self._state
