import pygame
from Game.Objects.Bullet.Bullet import Bullet
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant.EventEnum import EventEnum
from Game.Utils.Constant.SubEventEnum import SubEventEnum


class InstantBullet(Bullet):

    _size = 1

    def draw(self, screen):
        if self._state == self.NEW:
            pygame.draw.line(screen, (255, 255, 255), self.get_position(), self._target.get_center(), self._size)
            self._state = self.MOVING

    def update(self):
        if self._state == self.MOVING:
            EventDispatcher.dispatch(
                EventEnum.BULLET,
                {
                    "sub_event": SubEventEnum.ENEMY_HIT,
                    'bullet': self,
                    'damage': self._damage,
                    'target': self._target,
                }
            )
            self._state = self.TO_REMOVE
