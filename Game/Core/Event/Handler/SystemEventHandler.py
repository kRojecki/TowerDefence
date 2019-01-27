import pygame
import sys

from Core.Event.Handler.AbstractEventHandler import AbstractEventHandler


class SystemEventHandler(AbstractEventHandler):

    @classmethod
    def handle(cls, event) -> None:
        if event.type == pygame.QUIT:
            sys.exit(1)
