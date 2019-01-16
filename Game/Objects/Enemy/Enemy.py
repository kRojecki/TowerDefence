import pygame

from Objects.Interfaces.Drawable import Drawable
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant import EventEnum, Color
from Objects.Interfaces.Pathable import Pathable
from Utils.Constant import Position
import random


class Enemy(Drawable, Pathable):

    ALIVE = 0
    KILLED = 1

    _position = (60, 60)
    _size = (10, 10)

    _border_width = 2
    _move_vector = (0, 0)

    _overscreen_margin = 10

    _health = 100
    _speed = 0.25

    _rotation = 0

    _state = ALIVE

    def __init__(self, start_position, path):
        self._position = start_position
        self._path = path
        self._overscreen_margin = random.randrange(-30, -10)
        self._surface = pygame.Surface(self._size, pygame.SRCALPHA)

    def draw(self, screen):
        self._surface.fill(Color.CLEAR)
        if self._state != self.ALIVE:
            return

    def update(self):
        self._set_move_vector()

        if self._state == self.ALIVE:
            self._position = (
                self._position[Position.X] + (self._move_vector[Position.X] * self._speed),
                self._position[Position.Y] + (self._move_vector[Position.Y] * self._speed)
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

    def _set_move_vector(self):
        out_of_margin = self.get_position()[Position.X] < self._overscreen_margin \
                        or self.get_position()[Position.Y] < self._overscreen_margin

        self._move_vector = self._get_move_vector(out_of_margin)
