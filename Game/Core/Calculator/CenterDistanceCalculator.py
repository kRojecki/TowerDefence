from pygame import Vector2


class CenterDistanceCalculator:

    @staticmethod
    def calculate_distance(centerable_pos, target_pos):
        enemy_vector = Vector2(target_pos)
        self_vector = Vector2(centerable_pos)

        return enemy_vector.distance_to(self_vector)
