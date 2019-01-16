from Game.Utils.Constant import EventEnum
from Game.Core.Factory.TileFactory import TileFactory
from Game.Objects.Tile.Enum.TileEnum import TileEnum


class GameAreaHandler:

    _game_arena = None

    @staticmethod
    def handle(event):
        if event.type == EventEnum.TILE_CLICKED:
            GameAreaHandler._tile_clicked(event)


    @staticmethod
    def register_object(game_arena):
        GameAreaHandler._game_arena = game_arena

    @staticmethod
    def _tile_clicked(event):
        if event.tile.is_changeable():
            GameAreaHandler._game_arena.change_field(
                event.tile.get_tile_position(),
                TileFactory.create_tile_from_tile(event.tile, TileEnum.ROCKET_TURRET_TILE)
            )
