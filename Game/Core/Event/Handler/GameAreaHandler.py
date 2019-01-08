from Game.Utils.Constant import EventEnum
from Game.Core.Factory.TileFactory import TileFactory


class GameAreaHandler:

    _game_arena = 0

    @staticmethod
    def handle(event):
        if event.type == EventEnum.TILE_CLICKED:
            GameAreaHandler._game_arena.change_field(
                event.tile.get_tile_position(),
                TileFactory.create_tile_from_tile(event.tile, 'TurretTile')
            )
        if event.type == EventEnum.FIRE:
            pass
        if event.type == EventEnum.ENEMY_HIT:
            pass
        if event.type == EventEnum.ENEMY_KILLED:
            pass

    @staticmethod
    def register_object(game_arena):
        GameAreaHandler._game_arena = game_arena
