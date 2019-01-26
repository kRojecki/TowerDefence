from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Core.Factory.TileFactory import TileFactory
from Objects.Tile.Enum.TileEnum import TileEnum
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum
import Game.Objects.Tile.EmptyTile


class TileClickResolver:

    @staticmethod
    def resolve(event, level):
        tile = event.tile

        if not tile.is_changeable():
            return

        if not isinstance(tile, Game.Objects.Tile.EmptyTile.EmptyTile):
            EventDispatcher.dispatch(
                EventEnum.UI,
                SubEventEnum.SHOW_PANEL,
                {
                    'tile': tile,
                }
            )
            return

        if isinstance(tile, Game.Objects.Tile.EmptyTile.EmptyTile):
            level.change_field(
                event.tile.get_tile_position(),
                TileFactory.create_tile_from_tile(event.tile, TileEnum.ROCKET_TURRET_TILE)
            )
            return

