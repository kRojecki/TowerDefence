class PathStep:

    _move_vector = (0, 0)
    _distance_to_move = 0
    _tile_position = (0, 0)

    def __init__(self, distance_to_move, move_vector, tile_position):
        self._tile_position = tile_position
        self._distance_to_move = distance_to_move
        self._move_vector = move_vector

    def get_next_move(self):
        return self._move_vector

    def is_step_completed(self, moved_by):
        if moved_by >= self._distance_to_move:
            return True
        return False

    def get_tile_position(self):
        return self._tile_position
