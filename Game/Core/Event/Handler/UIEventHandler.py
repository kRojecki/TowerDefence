import pygame

import Game.Core.Event.Handler.MouseEventHandler as MouseHandler
from Core.Event.Handler.AbstractEventHandler import AbstractEventHandler
from Core.UI.Elements.TurretPanel import TurretPanel
from Utils.Constant.LayerEnum import LayerEnum


class UIEventHandler(AbstractEventHandler):

    _ui = None

    @staticmethod
    def register_object(level) -> None:
        UIEventHandler._ui = level

    @staticmethod
    def _add_score(event) -> None:
        UIEventHandler._ui.get_element('score').add(event.score)

    @staticmethod
    def _add_funds(event) -> None:
        UIEventHandler._ui.get_element('wallet').add(event.money)

    @staticmethod
    def _show_panel(event) -> None:

        UIEventHandler._set_clip(pygame.mouse.get_pos())
        UIEventHandler._set_active_layer(LayerEnum.PANEL)

        UIEventHandler._ui.add_element(
            event.tile.get_hash(),
            TurretPanel(event.tile)
        )

    @staticmethod
    def _hide_panel(event) -> None:

        UIEventHandler._set_clip((0, 0))
        UIEventHandler._set_active_layer(LayerEnum.TILE)

        UIEventHandler._ui.remove_panel()

    @staticmethod
    def _set_clip(position) -> None:
        MouseHandler.MouseEventHandler.set_clip(position)

    @staticmethod
    def _set_active_layer(layer) -> None:
        MouseHandler.MouseEventHandler.set_active_layer(layer)
