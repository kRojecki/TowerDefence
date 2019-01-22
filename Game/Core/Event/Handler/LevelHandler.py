from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Utils.Constant.Event.EventEnum import EventEnum
from Game.Core.Factory.TileFactory import TileFactory
from Game.Objects.Tile.Enum.TileEnum import TileEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


class LevelHandler:

    _level = None

    @staticmethod
    def handle(event):
        method_name = getattr(LevelHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def register_object(level):
        LevelHandler._level = level

    @staticmethod
    def _tile_clicked(event):
        if event.tile.is_changeable():
            LevelHandler._level.change_field(
                event.tile.get_tile_position(),
                TileFactory.create_tile_from_tile(event.tile, TileEnum.ROCKET_TURRET_TILE)
            )

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

