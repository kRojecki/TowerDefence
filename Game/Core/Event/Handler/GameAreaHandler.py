from Game.Utils.Constant import EventEnum
from Game.Core.Factory.TileFactory import TileFactory
from Game.Core.Factory.BulletFactory import BulletFactory
from Game.Objects.Tile.Enum.TileEnum import TileEnum


class GameAreaHandler:

    _game_arena = None

    @staticmethod
    def handle(event):
        if event.type == EventEnum.TILE_CLICKED:
            GameAreaHandler._game_arena.change_field(
                event.tile.get_tile_position(),
                TileFactory.create_tile_from_tile(event.tile, TileEnum.TURRET_TILE)
            )
        if event.type == EventEnum.ENEMY_KILLED:
            pass


    @staticmethod
    def register_object(game_arena):
        GameAreaHandler._game_arena = game_arena
