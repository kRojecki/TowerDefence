from Game.Utils.Constant import Position


class TilePositionCalculator:

    @staticmethod
    def calculate_position(tile):
        return ((tile.get_tile_position()[Position.Y] * tile.get_size()[Position.Y]),
                (tile.get_tile_position()[Position.X] * tile.get_size()[Position.X]))
