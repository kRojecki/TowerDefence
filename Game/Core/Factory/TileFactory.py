import Game.Core.GameArea
from Game.Objects.Tile.TurretTile import TurretTile
from Game.Objects.Tile.EmptyTile import EmptyTile


class TileFactory:

    @staticmethod
    def createTileFromTile(tile, tile_type):
        if tile_type == 'TurretTile':
            return TurretTile(tile.get_tile_position(), tile.get_size()[0], Game.Core.GameArea.GameArea.game_area_margin)
        else:
            return EmptyTile(tile.get_tile_position(), tile.get_size()[0], Game.Core.GameArea.GameArea.game_area_margin)
