from Game.Objects.Tile.Enum.TileEnum import TileEnum


class Default:
    MAP = {
        '0': TileEnum.EMPTY_TILE,
        '1': TileEnum.TURRET_TILE,
        '2': TileEnum.ENEMY_PATH_TILE,
        'S': TileEnum.ENEMY_STARTING_PATH_TILE,
        'E': TileEnum.ENEMY_END_PATH_TILE,
    }
