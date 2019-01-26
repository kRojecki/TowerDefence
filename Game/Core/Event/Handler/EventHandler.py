import pygame

from Core.Event.Handler.TileEventHandler import TileEventHandler
from Core.Event.Handler.UIEventHandler import UIEventHandler
from Utils.Constant.Event.EventEnum import EventEnum
from Game.Core.Event.Handler.MouseEventHandler import MouseEventHandler
from Game.Core.Event.Handler.SystemEventHandler import SystemEventHandler
from Game.Core.Event.Handler.LevelEventHandler import LevelEventHandler
from Game.Core.Event.Handler.EnemyEventHandler import EnemyEventHandler
from Game.Core.Event.Handler.BulletEventHandler import BulletEventHandler


class EventHandler:

    _handlers = {
        pygame.QUIT:                    SystemEventHandler,

        pygame.MOUSEBUTTONDOWN:         MouseEventHandler,
        pygame.MOUSEBUTTONUP:           MouseEventHandler,
        pygame.MOUSEMOTION:             MouseEventHandler,

        EventEnum.LEVEL:                LevelEventHandler,
        EventEnum.BULLET:               BulletEventHandler,
        EventEnum.ENEMY:                EnemyEventHandler,
        EventEnum.TILE:                 TileEventHandler,
        EventEnum.UI:                   UIEventHandler,
    }

    def init(self):
        MouseEventHandler.init()

    def handle(self):
        for event in pygame.event.get():
            if event.type in self._handlers:
                self._handlers[event.type].handle(event)
