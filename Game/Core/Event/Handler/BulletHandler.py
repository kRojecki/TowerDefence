from Game.Utils.Constant import EventEnum
from Game.Core.Factory.BulletFactory import BulletFactory


class BulletHandler:

    _bulletCollection = None

    @staticmethod
    def register_object(collection):
        BulletHandler._bulletCollection = collection

    @staticmethod
    def handle(event):
        if event.type == EventEnum.ENEMY_HIT:
            event.target.hit(event.damage)
            BulletHandler._bulletCollection.remove(event.bullet)

        if event.type == EventEnum.FIRE:
            BulletHandler._bulletCollection.append(
                BulletFactory.create_bullet_from_event(event)
            )

