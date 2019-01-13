from Game.Objects.Tile.Tile import Tile
from Game.Utils.Constant import Color, PointableState


class EmptyTile(Tile):

    _border_color = Color.T_EMPTY_TILE_BORDER

    _background_color = {
        PointableState.CLEAR: Color.T_EMPTY_TILE_BACKGROUND_CLEAR,
        PointableState.HOVER: Color.T_EMPTY_TILE_BACKGROUND_HOVER,
        PointableState.CLICKED: Color.T_EMPTY_TILE_BACKGROUND_CLICKED,
        }
