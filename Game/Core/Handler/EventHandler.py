import pygame
from Game.Core.Handler.MouseHandler import MouseHandler
from Game.Core.Handler.SystemHandler import SystemHandler


class EventHandler:

    _handlers = {
        pygame.MOUSEBUTTONDOWN : MouseHandler,
        pygame.MOUSEBUTTONUP : MouseHandler,
        pygame.MOUSEMOTION : MouseHandler,
        pygame.QUIT : SystemHandler,
    }

    def handle(self):
        for event in pygame.event.get():
            if event.type in self._handlers:
                print(self._handlers[event.type])
                self._handlers[event.type].handle(event)
