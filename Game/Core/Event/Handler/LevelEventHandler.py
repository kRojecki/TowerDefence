from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Core.Resolver.TileClickResolver import TileClickResolver
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


class LevelEventHandler:

    _level = None

    @staticmethod
    def handle(event):
        method_name = getattr(LevelEventHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def register_object(level):
        LevelEventHandler._level = level

    @staticmethod
    def _tile_clicked(event):
        EventDispatcher.dispatch(
            EventEnum.UI,
            SubEventEnum.HIDE_PANEL,
            {}
        )
        TileClickResolver.resolve(event, LevelEventHandler._level)

    @staticmethod
    def _enemy_completed_path(event):
        EventDispatcher.dispatch(
            EventEnum.ENEMY,
            SubEventEnum.ENEMY_REMOVE,
            {
                "enemy": event.enemy,
            }
        )
        EventDispatcher.dispatch(
            EventEnum.UI,
            SubEventEnum.ADD_SCORE,
            {
                "score": - event.enemy.get_score() * 5,
            }
        )

