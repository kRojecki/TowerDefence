
class NearestEnemyPositionCalculator:

    def calculate(self, tile, enemies):
        tile_pos = tile.get_position()

        return enemies.get(0)