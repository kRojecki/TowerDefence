import math
from Game.Utils.Constant import Position


class TileRotationCalculator:

    @staticmethod
    def calculate_rotation(tile, target):
        rel_y = target.get_center()[Position.Y] - tile.get_center()[Position.Y]
        rel_x = target.get_center()[Position.X] - tile.get_center()[Position.X]

        return ((180 / math.pi) * -math.atan2(rel_y, rel_x)) - 90

    @staticmethod
    def calculate_barrel_position(tile, rotation):

        center_point = tile.get_center()
        original_position = (tile.get_position()[Position.X] + (tile.get_size()[Position.X])-8, tile.get_position()[Position.Y] + (tile.get_size()[Position.Y])-10) #experimental values...
        radian_angle = (rotation - 228) * math.pi / 180

        x = (original_position[Position.X] - center_point[Position.X])*math.cos(radian_angle) + (original_position[Position.Y] - center_point[Position.Y])*math.sin(radian_angle) + center_point[Position.X]
        y = (original_position[Position.Y] - center_point[Position.Y])*math.cos(radian_angle) - (original_position[Position.Y] - center_point[Position.Y])*math.sin(radian_angle) + center_point[Position.Y]

        return (x, y)
