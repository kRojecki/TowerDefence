import Game.Core.Event.Handler.MouseEventHandler as MouseHandler
from Core.UI.Elements.TurretPanel import TurretPanel
from Utils.Constant.LayerEnum import LayerEnum


class UIEventHandler:

    _ui = None

    @staticmethod
    def handle(event):
        method_name = getattr(UIEventHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def register_object(level):
        UIEventHandler._ui = level

    @staticmethod
    def _add_score(event):
        UIEventHandler._ui.get_element('score').add(event.score)

    @staticmethod
    def _add_funds(event):
        UIEventHandler._ui.get_element('wallet').add(event.money)

    @staticmethod
    def _show_panel(event):

        UIEventHandler._set_clip(event.tile.get_center())
        UIEventHandler._set_active_layer(LayerEnum.PANEL)

        UIEventHandler._ui.add_element(
            event.tile.get_hash(),
            TurretPanel(event.tile)
        )

    @staticmethod
    def _hide_panel(event):

        UIEventHandler._set_clip((0, 0))
        UIEventHandler._set_active_layer(LayerEnum.TILE)

        UIEventHandler._ui.remove_panel()

    @staticmethod
    def _set_clip(position):
        MouseHandler.MouseEventHandler.set_clip(position)

    @staticmethod
    def _set_active_layer(layer):
        MouseHandler.MouseEventHandler.set_active_layer(layer)
