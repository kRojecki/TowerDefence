from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Core.Factory.TileFactory import TileFactory
from Objects.Tile.Enum.TileEnum import TileEnum
from Utils.Constant import MouseButtons
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum
import Game.Objects.Tile.EmptyTile


class TileClickResolver:

    @classmethod
    def resolve(cls, event, level):
        tile = event.tile
        buttons_pressed = event.buttons_pressed

        if buttons_pressed[MouseButtons.LEFT] == 1:
            cls.handle_left(tile, level)

        if buttons_pressed[MouseButtons.RIGHT] == 1:
            cls.handle_right(tile, level)

        if buttons_pressed[MouseButtons.MIDDLE] == 1:
            cls.handle_middle(tile, level)

    @classmethod
    def handle_left(cls, tile, level):
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
                tile.get_tile_position(),
                TileFactory.create_tile_from_tile(tile, TileEnum.ROCKET_TURRET_TILE)
            )
            return

    @classmethod
    def handle_right(cls, tile, level):
        pass

    @classmethod
    def handle_middle(cls, tile, level):
        pass
