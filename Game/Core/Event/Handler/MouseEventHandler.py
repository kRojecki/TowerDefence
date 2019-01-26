import pygame

import Objects.Abstracts.Pointerable
from Utils.Helper.DataSetHelper.TupleTransformer import TupleTransformer


class MouseEventHandler:
    _pointerable_objects = [[], []]

    _clip = (0, 0)
    _active_layer = 0

    @staticmethod
    def init():
        MouseEventHandler._pointerable_objects.append([])
        MouseEventHandler._pointerable_objects.append([])

    @staticmethod
    def handle(event):
        mouse_position = MouseEventHandler._get_mouse_position()
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in MouseEventHandler._pointerable_objects[MouseEventHandler._active_layer]:
                sprite.on_hover(mouse_position)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sprite.on_click(mouse_position)

    @staticmethod
    def register_object(object, layer=0):
        if isinstance(object, Objects.Abstracts.Pointerable.Pointerable):
            MouseEventHandler._pointerable_objects[layer].append(object)

    @staticmethod
    def set_clip(position):
        MouseEventHandler._clip = position

    @staticmethod
    def set_active_layer(layer):
        MouseEventHandler._active_layer = layer

    @staticmethod
    def _get_mouse_position():
        return TupleTransformer.add_tuples(pygame.mouse.get_pos(), TupleTransformer.negate_tuple(MouseEventHandler._clip))
