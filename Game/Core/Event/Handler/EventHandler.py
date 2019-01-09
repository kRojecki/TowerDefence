import pygame
from Game.Utils.Constant import EventEnum
from Game.Core.Event.Handler.MouseHandler import MouseHandler
from Game.Core.Event.Handler.SystemHandler import SystemHandler
from Game.Core.Event.Handler.GameAreaHandler import GameAreaHandler
from Game.Core.Event.Handler.EnemyHandler import EnemyHandler
from Game.Core.Event.Handler.BulletHandler import BulletHandler


class EventHandler:

    _handlers = {
        pygame.MOUSEBUTTONDOWN: MouseHandler,
        pygame.MOUSEBUTTONUP:   MouseHandler,
        pygame.MOUSEMOTION:     MouseHandler,
        pygame.QUIT:            SystemHandler,

        EventEnum.TILE_CLICKED: GameAreaHandler,
        EventEnum.FIRE:         BulletHandler,
        EventEnum.ENEMY_HIT:    BulletHandler,
        EventEnum.ENEMY_KILLED: EnemyHandler,
    }

    def handle(self):
        for event in pygame.event.get():
            if event.type in self._handlers:
                self._handlers[event.type].handle(event)
