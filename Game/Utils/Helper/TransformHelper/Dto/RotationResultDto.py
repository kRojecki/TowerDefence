class RotationResultDto:

    transformed_surface = 0
    position_modifier = ()

    def __init__(self, transformed_surface, position_modifier):
        self.transformed_surface = transformed_surface
        self.position_modifier = position_modifier
