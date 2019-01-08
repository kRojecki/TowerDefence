import pygame
import Game.Objects.Pointerable


class MouseHandler:

    _pointerable_objects = []

    @staticmethod
    def handle(event):
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in MouseHandler._pointerable_objects:
                sprite.on_hover()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sprite.on_click()

    @staticmethod
    def register_object(object):
        if isinstance(object, Game.Objects.Pointerable.Pointerable):
            MouseHandler._pointerable_objects.append(object)
