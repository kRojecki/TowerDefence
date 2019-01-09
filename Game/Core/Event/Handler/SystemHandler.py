import pygame
import sys


class SystemHandler:

    @staticmethod
    def handle(event):
        if event.type == pygame.QUIT:
            sys.exit(1)
