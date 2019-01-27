from Core.Event.Handler.AbstractEventHandler import AbstractEventHandler
from Game.Core.Factory.BulletFactory import BulletFactory


class BulletEventHandler(AbstractEventHandler):

    _bulletCollection = None

    @staticmethod
    def register_object(collection) -> None:
        BulletEventHandler._bulletCollection = collection


    @staticmethod
    def _enemy_hit(event) -> None:
        event.target.hit(event.damage)
        BulletEventHandler._bulletCollection.remove(event.bullet)

    @staticmethod
    def _fire(event) -> None:
        BulletEventHandler._bulletCollection.append(
            BulletFactory.create_bullet_from_event(event)
        )
