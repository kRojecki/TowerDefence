from Game.Objects.Tile.TurretTile import TurretTile
from Game.Objects.Tile.EmptyTile import EmptyTile


class TileFactory:

    @staticmethod
    def create_tile_from_tile(tile, tile_type):
        return TileFactory.create_tile_from_args(tile.get_tile_position(), tile.get_size()[0], tile_type)

    @staticmethod
    def create_tile_from_args(position, size, tile_type):
        if tile_type == 'TurretTile':
            return TurretTile(position, size)
        else:
            return EmptyTile(position, size)
