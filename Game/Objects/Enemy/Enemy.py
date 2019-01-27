import random

import pygame

import Core.Level.Level
from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant import Color
from Objects.Abstracts.Drawable import Drawable
from Objects.Abstracts.Enemy.Healthable import Healthable
from Objects.Abstracts.Enemy.Pathable import Pathable
from Utils.Constant import Position
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


class Enemy(Drawable, Pathable, Healthable):

    _position = (60, 60)
    _size = (10, 10)

    _border_width = 2
    _move_vector = (0, 0)

    _overscreen_margin = 10

    _speed = 0.25

    _max_health = 100

    _score = 10
    _money = 15

    def __init__(self, start_position, path):
        super().__init__()
        self._position = start_position
        self._path = path
        self._overscreen_margin = random.randrange(-30, -10)
        self._surface = pygame.Surface(self._size, pygame.SRCALPHA)

    def draw(self, screen):
        if self._state != self.ALIVE:
            return

        self._surface.fill(Color.CLEAR)
        screen.blit(self._draw_health_bar(self._size[0]), self._get_health_bar_position())

    def update(self):

        if self._state != self.ALIVE:
            return

        self._set_move_vector()

        self._position = (
            self._position[Position.X] + (self._move_vector[Position.X] * self._speed),
            self._position[Position.Y] + (self._move_vector[Position.Y] * self._speed)
        )

        if self._completed_path():
            self._state = self.COMPLETED
            EventDispatcher.dispatch(
                EventEnum.LEVEL,
                SubEventEnum.ENEMY_COMPLETED_PATH,
                {
                    "enemy": self,
                }
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
            EventEnum.ENEMY,
            SubEventEnum.ENEMY_KILLED,
            {
                'enemy': self,
            }
        )

    def _completed_path(self):
        return self.get_center()[Position.X] > Core.Level.Level.Level.area_size[Position.X] \
               or self.get_center()[Position.Y] > Core.Level.Level.Level.area_size[Position.Y]

    def get_score(self):
        return self._score

    def get_money(self):
        return self._money
