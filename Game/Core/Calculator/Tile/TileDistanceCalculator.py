import pygame


class TileDistanceCalculator:

    @staticmethod
    def calculate_distance(tile, target):
        enemy_vector = pygame.Vector2(target.get_center())
        self_vector = pygame.Vector2(tile.get_center())

        return enemy_vector.distance_to(self_vector)
