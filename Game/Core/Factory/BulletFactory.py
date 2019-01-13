from Game.Utils.Helper.ClassProvider import ClassProvider


class BulletFactory:

    DEFAULT_BULLET = 'Game.Objects.Bullet.InstantBullet.InstantBullet'

    @staticmethod
    def create_bullet_from_event(event):
        return BulletFactory.create_bullet_from_args(event.start_position, event.enemy)

    @staticmethod
    def create_bullet_from_args(position, target, bullet_type=DEFAULT_BULLET):
        return ClassProvider.provide_class(bullet_type)(position, target)
