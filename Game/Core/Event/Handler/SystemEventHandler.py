import pygame
import sys

from Core.Event.Handler.AbstractEventHandler import AbstractEventHandler


class SystemEventHandler(AbstractEventHandler):

    @staticmethod
    def handle(event) -> None:
        if event.type == pygame.QUIT:
            sys.exit(1)
