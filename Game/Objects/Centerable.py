from Game.Utils.Constant import Position


class Centerable:

    _position = ()
    _size = ()

    def get_center(self):
        return (
            (int) (self._position[Position.X] + self._size[Position.X] / 2),
            (int) (self._position[Position.Y] + self._size[Position.Y] / 2),
        )
