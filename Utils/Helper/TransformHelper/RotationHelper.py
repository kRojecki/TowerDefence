import pygame
import math
from Utils.Helper.TransformHelper.Dto.RotationResultDto import RotationResultDto

class RotationHelper:

    @staticmethod
    def rotate(surface, angle):

        rotatedSurface = pygame.transform.rotate(surface, angle)

        originalRect = surface.get_rect()
        originalRectCenter = (originalRect.width /2, originalRect.height /2)

        rotatedRect = rotatedSurface.get_rect()
        transformedRectCenter = (rotatedRect.width /2, rotatedRect.height /2)

        positionModifier = (math.floor(transformedRectCenter[0] - originalRectCenter[0]), math.floor(transformedRectCenter[1] - originalRectCenter[1]));

        return RotationResultDto(rotatedSurface, positionModifier)
