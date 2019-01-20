from Game.Core.Factory.BulletFactory import BulletFactory


class BulletHandler:

    _bulletCollection = None

    @staticmethod
    def register_object(collection):
        BulletHandler._bulletCollection = collection

    @staticmethod
    def handle(event):
        method_name = getattr(BulletHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def _enemy_hit(event):
        event.target.hit(event.damage)
        BulletHandler._bulletCollection.remove(event.bullet)

    @staticmethod
    def _fire(event):
        BulletHandler._bulletCollection.append(
            BulletFactory.create_bullet_from_event(event)
        )
