import pygame
from Game.Objects.Bullet.Bullet import Bullet
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Utils.Constant import EventEnum


class InstantBullet(Bullet):

    def draw(self, screen):
        if self._state == self.NEW:
            pygame.draw.line(screen, (255, 255, 255), self.get_position(), self._target.get_center(), 1)
            self._state = self.MOVING

    def update(self):
        if self._state == self.MOVING:
            EventDispatcher.dispatch(
                EventEnum.ENEMY_HIT,
                {
                    'bullet': self,
                    'damage': self._damage,
                    'target': self._target,
                }
            )
            self._state = self.TO_REMOVE
