from Game.Utils.Helper.ClassProvider import ClassProvider
from Utils.Constant import Position


class TileFactory:

    @staticmethod
    def create_tile_from_tile(tile, tile_type):
        # change coordinates because of array
        tile_pos = (
            tile.get_tile_position()[Position.Y],
            tile.get_tile_position()[Position.X]
        )

        return TileFactory.create_tile_from_args(tile_pos, tile.get_size()[0], tile_type)

    @staticmethod
    def create_tile_from_args(position, size, tile_type):
            return ClassProvider.provide_class(tile_type)(position, size)

