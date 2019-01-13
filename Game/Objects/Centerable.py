from Game.Utils.Constant import Position


class Centerable:

    _position = (0, 0)
    _size = (0, 0)

    def get_position(self):
        return (
            int(self._position[Position.X]),
            int(self._position[Position.Y])
        )

    def get_size(self):
        return self._size

    def get_center(self):
        return (
            (int) (self._position[Position.X] + self._size[Position.X] / 2),
            (int) (self._position[Position.Y] + self._size[Position.Y] / 2),
        )
