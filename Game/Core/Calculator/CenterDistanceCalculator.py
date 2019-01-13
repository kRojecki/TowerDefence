import pygame


class CenterDistanceCalculator:

    @staticmethod
    def calculate_distance(centerable, target):
        enemy_vector = pygame.Vector2(target.get_center())
        self_vector = pygame.Vector2(centerable.get_center())

        return enemy_vector.distance_to(self_vector)
