import pygame

from Core.Event.Handler.UIHandler import UIHandler
from Utils.Constant.Event.EventEnum import EventEnum
from Game.Core.Event.Handler.MouseHandler import MouseHandler
from Game.Core.Event.Handler.SystemHandler import SystemHandler
from Game.Core.Event.Handler.LevelHandler import LevelHandler
from Game.Core.Event.Handler.EnemyHandler import EnemyHandler
from Game.Core.Event.Handler.BulletHandler import BulletHandler


class EventHandler:

    _handlers = {
        pygame.QUIT:                    SystemHandler,

        pygame.MOUSEBUTTONDOWN:         MouseHandler,
        pygame.MOUSEBUTTONUP:           MouseHandler,
        pygame.MOUSEMOTION:             MouseHandler,

        EventEnum.LEVEL:                LevelHandler,
        EventEnum.BULLET:               BulletHandler,
        EventEnum.ENEMY:                EnemyHandler,
        EventEnum.UI:                   UIHandler,
    }

    def init(self):
        MouseHandler.init()

    def handle(self):
        for event in pygame.event.get():
            if event.type in self._handlers:
                self._handlers[event.type].handle(event)
