import pygame
from Game.Utils.Constant import EventEnum
from Game.Core.Handler.MouseHandler import MouseHandler
from Game.Core.Handler.SystemHandler import SystemHandler
from Game.Core.Handler.GameAreaHandler import GameAreaHandler


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
            print(event)
            if event.type in self._handlers:
                print(self._handlers[event.type])
                self._handlers[event.type].handle(event)
