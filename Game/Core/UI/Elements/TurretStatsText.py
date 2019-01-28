from Core.UI.Elements.Abstract.Text import Text
from Core.UI.Elements.IntLabel import IntLabel


class TurretStatsText(Text):

    _turret = None

    _stat_rows = None

    def __init__(self, position, turret) -> None:
        super().__init__()
        self._position = position
        self._turret = turret
        self._stat_rows = dict()
        self.init()

    def init(self):
        self._stat_rows.clear()
        self._stat_rows.update({
            'damage': IntLabel((5, 5), "Damage: ", self._turret.get_damage()),
            'range': IntLabel((5, 20), "Range: ", self._turret.get_range()),
            'fire_rate': IntLabel((5, 35), "Fire rate: ", self._turret.get_fire_rate()),
            'level': IntLabel((55, 75), "", self._turret.get_level()),
        })

    def draw(self, screen):
        self.update()
        for key, element in self._stat_rows.items():
            element.draw(screen)

    def update(self):
        self._stat_rows.get('damage').set_value(self._turret.get_damage())
        self._stat_rows.get('range').set_value(self._turret.get_range())
        self._stat_rows.get('fire_rate').set_value(self._turret.get_fire_rate())
        self._stat_rows.get('level').set_value(self._turret.get_level())
