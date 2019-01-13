from Game.Objects.Tile.Tile import Tile
from Game.Utils.Constant import Color, PointableState


class EnemyPath(Tile):

    _border_color = Color.T_ENEMY_PATH_TILE_BORDER

    _background_color = {
        PointableState.CLEAR: Color.T_ENEMY_PATH_TILE_BACKGROUND_CLEAR,
        PointableState.HOVER: Color.T_ENEMY_PATH_TILE_BACKGROUND_HOVER,
        PointableState.CLICKED: Color.T_ENEMY_PATH_TILE_BACKGROUND_CLICKED,
        }

    _changeable = False
