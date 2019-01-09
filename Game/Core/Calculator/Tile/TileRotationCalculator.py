import math
from Game.Utils.Constant import Position


class TileRotationCalculator:

    @staticmethod
    def calculate_rotation(tile, target):
        rel_y = target.get_center()[Position.Y] - tile.get_center()[Position.Y]
        rel_x = target.get_center()[Position.X] - tile.get_center()[Position.X]

        return ((180 / math.pi) * -math.atan2(rel_y, rel_x)) - 90
