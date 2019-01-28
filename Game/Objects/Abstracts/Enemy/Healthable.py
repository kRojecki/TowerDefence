import math
import pygame

from Utils.Constant import Color


class Healthable:
    ALIVE = 0
    KILLED = 1
    COMPLETED = 2

    _state = ALIVE
    _max_health = 100
    _health = 0

    def __init__(self):
        self._health = self._max_health

    def hit(self, damage):
        self._health = self._health - damage
        if self._health <= 0:
            self._death()

    def _death(self):
        self._state = self.KILLED

    def get_state(self):
        return self._state

    def _draw_health_bar(self, max_bar_size):
        health_bar_length = math.floor(self._get_health_percentage() * max_bar_size)

        bar_surface = pygame.Surface((max_bar_size, 2))
        pygame.draw.line(bar_surface, Color.BLACK, (0, 0), (max_bar_size, 0), 2)
        pygame.draw.line(bar_surface, self._get_health_color(), (0, 0), (health_bar_length, 0), 2)
        return bar_surface

    def _get_health_percentage(self):
        return self._health / self._max_health

    def _get_health_color(self):
        health_remaining = self._health / self._max_health
        if health_remaining > 0.75:
            return Color.GREEN
        if health_remaining > 0.5:
            return Color.YELLOW
        if health_remaining > 0.25:
            return Color.ORANGE
        return Color.RED

    def _get_health_bar_position(self):
        raise Exception("Must implement Healthable._get_health_bar_position method!")
