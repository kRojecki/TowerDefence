class Path:

    _steps = ()

    def __init__(self, steps):
        self._steps = steps

    def get_next_move(self, step, moved_by):
        previous_step = step

        if self._steps[step].is_step_completed(moved_by):
            step += 1

        move_vector = self._steps[step].get_next_move()

        return [move_vector, step, step != previous_step]
