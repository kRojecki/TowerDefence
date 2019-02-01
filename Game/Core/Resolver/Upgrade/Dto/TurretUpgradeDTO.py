class TurretUpgradeDTO:

    _range = 0
    _damage = 0
    _fire_rate = 0

    def __init__(self, values: dict):
        self._range = values.get('range')
        self._damage = values.get('damage')
        self._fire_rate = values.get('fire_rate')

    def get_range(self):
        return self._range

    def get_damage(self):
        return self._damage

    def get_fire_rate(self):
        return self._fire_rate
