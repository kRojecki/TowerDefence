class Upgradeable:

    _upgrade_level = 0

    def upgrade(self, upgrade_dto):

        self._upgrade_stats(upgrade_dto)
        self._upgrade_level += 1

        pass

    def _upgrade_stats(self, upgrade_dto):
        pass

    def get_level(self):
        return self._upgrade_level + 1
