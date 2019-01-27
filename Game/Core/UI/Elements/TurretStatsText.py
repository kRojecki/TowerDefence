from Core.UI.Elements.Abstract.Text import Text
from Core.UI.Elements.IntLabel import IntLabel


class TurretStatsText(Text):

    _turret = None

    _stat_rows = []

    def __init__(self, position, turret) -> None:
        self._position = position
        self._turret = turret
        self.init()

    def init(self):
        self._stat_rows.append(
            IntLabel((5, 5), "Damage: ", self._turret.get_damage())
        )
        self._stat_rows.append(
            IntLabel((5, 20), "Range: ", self._turret.get_range())
        )
        self._stat_rows.append(
            IntLabel((5, 35), "Fire rate: ", self._turret.get_fire_rate())
        )

    def draw(self, screen):
        for element in self._stat_rows:
            element.draw(screen)
