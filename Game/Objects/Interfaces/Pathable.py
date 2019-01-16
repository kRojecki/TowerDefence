class Pathable:

    _path = None
    _current_path_step = 0
    _step_move_count = 0
    _speed = 0

    def _get_move_vector(self, block_counter=False):
        move_vector, self._current_path_step, reset_count = self._path.get_next_move(self._current_path_step,
                                                                                     self._step_move_count)
        if reset_count:
            self._step_move_count = 0

        if not block_counter:
            self._step_move_count += self._speed

        return move_vector
