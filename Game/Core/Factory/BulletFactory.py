from Game.Utils.Helper.ClassProvider import ClassProvider
from Objects.Bullet.Enum.BulletEnum import BulletEnum


class BulletFactory:

    DEFAULT_BULLET = BulletEnum.INSTANT_BULLET

    @staticmethod
    def create_bullet_from_event(event):
        return BulletFactory.create_bullet_from_args(event.start_position, event.enemy, event.damage, event.bullet_type)

    @staticmethod
    def create_bullet_from_args(position, target, damage, bullet_type=DEFAULT_BULLET):
        return ClassProvider.provide_class(bullet_type)(position, target, damage)
