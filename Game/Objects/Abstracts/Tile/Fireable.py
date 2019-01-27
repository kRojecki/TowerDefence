from Objects.Bullet.Enum.BulletEnum import BulletEnum


class Fireable:
    _damage = 0
    _fire_rate = 0
    _range = 0

    _bullet_type = BulletEnum.INSTANT_BULLET

    def get_damage(self):
        return self._damage

    def get_range(self):
        return self._range

    def get_fire_rate(self):
        return self._fire_rate
