import pygame
import math
from Utils.Helper.TransformHelper.Dto.RotationResultDto import RotationResultDto


class RotationHelper:

    @staticmethod
    def rotate(surface, angle):

        rotated_surface = pygame.transform.rotate(surface, angle)

        original_rect = surface.get_rect()
        original_rect_center = (original_rect.width / 2, original_rect.height / 2)

        rotated_rect = rotated_surface.get_rect()
        transformed_rect_center = (rotated_rect.width / 2, rotated_rect.height / 2)

        position_modifier = (
            math.floor(transformed_rect_center[0] - original_rect_center[0]),
            math.floor(transformed_rect_center[1] - original_rect_center[1])
        )

        return RotationResultDto(rotated_surface, position_modifier)
