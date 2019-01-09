import pygame
from Game.Utils.Constant import EventEnum
from Game.Core.Event.Handler.MouseHandler import MouseHandler
from Game.Core.Event.Handler.SystemHandler import SystemHandler
from Game.Core.Event.Handler.GameAreaHandler import GameAreaHandler


class EventHandler:

    _handlers = {
        pygame.MOUSEBUTTONDOWN: MouseHandler,
        pygame.MOUSEBUTTONUP: MouseHandler,
        pygame.MOUSEMOTION: MouseHandler,
        pygame.QUIT: SystemHandler,
        EventEnum.TILE_CLICKED: GameAreaHandler,
    }

    def handle(self):
        for event in pygame.event.get():
            if event.type in self._handlers:
                self._handlers[event.type].handle(event)
