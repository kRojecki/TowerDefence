from Core.Event.Handler.AbstractEventHandler import AbstractEventHandler
from Core.Resolver.TurretUpgradeResolver import TurretUpgradeResolver


class TileEventHandler(AbstractEventHandler):


    @staticmethod
    def _turret_upgrade(event) -> None:
        event.tile.upgrade(TurretUpgradeResolver.resolve(event.tile))
        pass


