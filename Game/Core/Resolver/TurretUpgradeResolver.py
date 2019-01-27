from Core.Resolver.Dto.TurretUpgradeDTO import TurretUpgradeDTO


class TurretUpgradeResolver:

    @classmethod
    def resolve(cls, tile):
        return TurretUpgradeDTO(
            tile.get_range(),
            tile.get_damage() + 1,
            tile.get_fire_rate()
        )
