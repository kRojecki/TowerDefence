class TurretUpgradeDTO:

    _range = 0
    _damage = 0
    _fire_rate = 0

    def __init__(self, range, damage, fire_rate):
        self._range = range
        self._damage = damage
        self._fire_rate = fire_rate

    def get_range(self):
        return self._range

    def get_damage(self):
        return self._damage

    def get_fire_rate(self):
        return self._fire_rate
