import pygame
from Game.Objects.Drawable import Drawable
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant import EventEnum, Color


class Enemy(Drawable):

    ALIVE = 0
    KILLED = 1

    _position = (60, 60)
    _size = (5, 5)

    _health = 100
    _speed = 1

    _state = ALIVE

    def draw(self, screen):
        if self._state == self.ALIVE:
            pygame.draw.circle(screen, Color.WHITE, self._position, self._size[0], 1)

    def update(self):
        if self._state == self.ALIVE:
            self._position = pygame.mouse.get_pos()

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
