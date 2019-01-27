import pygame

import Objects.Abstracts.Pointerable
from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Core.UI.Elements.TurretPanel import TurretPanel
from Utils.Constant import Position
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum
from Utils.Constant.LayerEnum import LayerEnum
from Utils.Helper.DataSetHelper.TupleTransformer import TupleTransformer


class MouseEventHandler:
    _pointerable_objects = [[], []]

    _clip = pygame.Rect((0, 0), (0, 0))
    _active_layer = LayerEnum.TILE

    @staticmethod
    def handle(event):
        mouse_position = MouseEventHandler._get_mouse_position()

        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseEventHandler._try_hide_panel()

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
        MouseEventHandler._clip = pygame.Rect(position, TurretPanel.get_clip_size())

    @staticmethod
    def set_active_layer(layer):
        MouseEventHandler._active_layer = layer

    @staticmethod
    def _get_mouse_position():
        return TupleTransformer.add_tuples(
            pygame.mouse.get_pos(),
            TupleTransformer.negate_tuple((MouseEventHandler._clip.x, MouseEventHandler._clip.y)))

    @staticmethod
    def _try_hide_panel():
        if MouseEventHandler._is_out_of_panel():
            EventDispatcher.dispatch(
                EventEnum.UI,
                SubEventEnum.HIDE_PANEL,
                {}
            )
            return

    @staticmethod
    def _is_out_of_panel():
        if MouseEventHandler._active_layer == LayerEnum.TILE:
            return False

        mouse_position = MouseEventHandler._get_mouse_position()
        return MouseEventHandler._clip.width < mouse_position[Position.X] \
               or MouseEventHandler._clip.height < mouse_position[Position.Y] \
               or 0 > mouse_position[Position.X] or 0 > mouse_position[Position.Y]
