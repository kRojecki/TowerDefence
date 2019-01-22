from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Utils.Constant.Event.EventEnum import EventEnum
from Game.Core.Factory.TileFactory import TileFactory
from Game.Objects.Tile.Enum.TileEnum import TileEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


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
        UIHandler._ui.get_element('score').add_score(event.score)    \

    @staticmethod
    def _add_funds(event):
        UIHandler._ui.get_element('wallet').add_funds(event.money)
