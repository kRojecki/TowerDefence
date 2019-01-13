class NearestEnemyPositionCalculator:

    _enemies = None

    def __init__(self, enemies):
        self._enemies = enemies

    def calculate(self, tile):

        if len(self._enemies) == 0:
            return None

        return self._enemies.get(0)
