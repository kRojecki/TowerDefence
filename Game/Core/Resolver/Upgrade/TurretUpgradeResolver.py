from Core.Resolver.Upgrade.Dto.TurretUpgradeDTO import TurretUpgradeDTO
from Core.Resolver.Upgrade.GrowthFunctions.Constant import Constant
from Core.Resolver.Upgrade.GrowthFunctions.ExponentialIncrement import ExponentialIncrement
from Core.Resolver.Upgrade.GrowthFunctions.LinearIncrement import LinearIncrement
from Objects.Tile.Enum.TileEnum import TileEnum


class TurretUpgradeResolver:

    _growth_definitions = {
        TileEnum.SMALL_TURRET_TILE_SHORT: {
            'range': Constant(),
            'damage': LinearIncrement(1),
            'fire_rate': Constant(),
        },
        TileEnum.ROCKET_TURRET_TILE_SHORT: {
            'range': LinearIncrement(1),
            'damage': ExponentialIncrement(2),
            'fire_rate': Constant(),
        }
    }

    @classmethod
    def resolve(cls, tile):
        name = tile.__class__.__name__

        functions = cls._growth_definitions.get(name)
        values = cls._generate_values(tile, functions)

        return cls._prepare_dto(values)

    @classmethod
    def _generate_values(cls, tile, functions):
        values = {}

        for key, function in functions.items():
            method_name = getattr(tile, 'get_' + key)
            values.update({
                key: function.calculate_growth(method_name(), tile.get_level())
            })

        return values

    @classmethod
    def _prepare_dto(cls, values):
        return TurretUpgradeDTO(values)
