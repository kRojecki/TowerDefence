from Game.Utils.Helper.ClassProvider import ClassProvider


class TileFactory:

    @staticmethod
    def create_tile_from_tile(tile, tile_type):
        return TileFactory.create_tile_from_args(tile.get_tile_position(), tile.get_size()[0], tile_type)

    @staticmethod
    def create_tile_from_args(position, size, tile_type):
            return ClassProvider.provide_class(tile_type)(position, size)

