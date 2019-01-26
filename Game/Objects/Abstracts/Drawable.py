from Objects.Abstracts.Centerable import Centerable
from Utils.Constant import Position
from Utils.Helper.DataSetHelper.TupleTransformer import TupleTransformer
from Utils.Helper.TransformHelper.RotationHelper import RotationHelper


class Drawable(Centerable):

    _surface = None
    _rotation = 0

    _global_position = (0, 0)

    def draw(self, screen):
        pass

    def blit(self, screen):
        rotated_surface, blit_destination = self._rotate()
        screen.blit(rotated_surface, blit_destination)

    def _rotate(self):
        if self._rotation != 0:
            rotation_dto = RotationHelper.rotate(self._surface, self._rotation)

            blit_destination = (self._position[Position.X] - rotation_dto.position_modifier[Position.X],
                                self._position[Position.Y] - rotation_dto.position_modifier[Position.Y])
            return [rotation_dto.transformed_surface, blit_destination]
        else:
            return [self._surface, self._position]

    def _update_global_position(self):
        self._global_position = TupleTransformer.add_tuples(self._global_position, self.get_position())
        pass
