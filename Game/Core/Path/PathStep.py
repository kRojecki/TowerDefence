class PathStep:

    _move_vector = (0, 0)
    _position_condition = (0, 0)
    _tile_position = (0, 0)

    def __init__(self, position_condition, move_vector, tile_position):
        self._tile_position = tile_position
        self._position_condition = position_condition
        self._move_vector = move_vector

    def get_next_move(self):
        return self._move_vector

    def is_step_completed(self, moved_by):
        if moved_by >= self._position_condition:
            return True
        return False

    def get_tile_position(self):
        return self._tile_position
