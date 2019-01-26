from Game.Core.Factory.BulletFactory import BulletFactory


class BulletEventHandler:

    _bulletCollection = None

    @staticmethod
    def register_object(collection):
        BulletEventHandler._bulletCollection = collection

    @staticmethod
    def handle(event):
        method_name = getattr(BulletEventHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def _enemy_hit(event):
        event.target.hit(event.damage)
        BulletEventHandler._bulletCollection.remove(event.bullet)

    @staticmethod
    def _fire(event):
        BulletEventHandler._bulletCollection.append(
            BulletFactory.create_bullet_from_event(event)
        )
