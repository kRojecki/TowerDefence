from Core.Calculator.CenterDistanceCalculator import CenterDistanceCalculator
from Game.Objects.Enemy.Enemy import Enemy


class NearestEnemyPositionCalculator:

    _enemies = None

    def __init__(self, enemies):
        self._enemies = enemies

    def calculate(self, tile):

        if len(self._enemies) == 0:
            return None

        nearest = None
        nearest_distance = None

        for enemy in self._enemies.get_elements():

            if not isinstance(enemy, Enemy):
                continue

            if nearest is None:
                nearest = enemy
                nearest_distance = CenterDistanceCalculator.calculate_distance(tile, enemy)
                continue

            new_distance = CenterDistanceCalculator.calculate_distance(tile, enemy)
            if new_distance < nearest_distance:
                nearest = enemy
                nearest_distance = new_distance
                continue

        return nearest
