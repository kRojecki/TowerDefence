import pygame
import sys


class SystemEventHandler:

    @staticmethod
    def handle(event):
        if event.type == pygame.QUIT:
            sys.exit(1)
