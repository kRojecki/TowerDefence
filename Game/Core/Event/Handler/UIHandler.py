import Game.Core.Event.Handler.MouseHandler as MouseHandler
from Core.UI.Elements.TurretPanel import TurretPanel
from Utils.Constant.LayerEnum import LayerEnum


class UIHandler:

    _ui = None

    @staticmethod
    def handle(event):
        method_name = getattr(UIHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def register_object(level):
        UIHandler._ui = level

    @staticmethod
    def _add_score(event):
        UIHandler._ui.get_element('score').add(event.score)

    @staticmethod
    def _add_funds(event):
        UIHandler._ui.get_element('wallet').add(event.money)

    @staticmethod
    def _show_panel(event):

        UIHandler._set_clip(event.tile.get_center())
        UIHandler._set_active_layer(LayerEnum.PANEL)

        UIHandler._ui.add_element(
            event.tile.get_hash(),
            TurretPanel(event.tile)
        )

    @staticmethod
    def _hide_panel(event):

        UIHandler._set_clip((0, 0))
        UIHandler._set_active_layer(LayerEnum.TILE)

        UIHandler._ui.remove_panel()

    @staticmethod
    def _set_clip(position):
        MouseHandler.MouseHandler.set_clip(position)

    @staticmethod
    def _set_active_layer(layer):
        MouseHandler.MouseHandler.set_active_layer(layer)
