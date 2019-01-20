import pygame

from Objects.Abstracts.Drawable import Drawable
from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant import EventEnum, Color
from Objects.Abstracts.Healthable import Healthable
from Objects.Abstracts.Pathable import Pathable
from Utils.Constant import Position
import random


class Enemy(Drawable, Pathable, Healthable):

    _position = (60, 60)
    _size = (10, 10)

    _border_width = 2
    _move_vector = (0, 0)

    _overscreen_margin = 10

    _speed = 0.25

    _max_health = 100

    def __init__(self, start_position, path):
        super().__init__()
        self._position = start_position
        self._path = path
        self._overscreen_margin = random.randrange(-30, -10)
        self._surface = pygame.Surface(self._size, pygame.SRCALPHA)

    def draw(self, screen):
        self._surface.fill(Color.CLEAR)
        screen.blit(self._draw_health_bar(self._size[0]), self._get_health_bar_position())
        if self._state != self.ALIVE:
            return

    def update(self):
        self._set_move_vector()

        if self._state == self.ALIVE:
            self._position = (
                self._position[Position.X] + (self._move_vector[Position.X] * self._speed),
                self._position[Position.Y] + (self._move_vector[Position.Y] * self._speed)
            )

    def _set_move_vector(self):
        out_of_margin = self.get_position()[Position.X] < self._overscreen_margin \
                        or self.get_position()[Position.Y] < self._overscreen_margin

        self._move_vector = self._get_move_vector(out_of_margin)

    def _get_health_bar_position(self):
        return (
            self.get_position()[Position.X],
            self.get_position()[Position.Y] - 5
        )

    def _death(self):
        super()._death()
        EventDispatcher.dispatch(
            EventEnum.ENEMY_KILLED,
            {
                'enemy': self,
            }
        )
