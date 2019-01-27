from Objects.Abstracts.Drawable import Drawable


class Bullet(Drawable):

    NEW = 0
    MOVING = 1
    TO_REMOVE = 2

    _position = (10, 10)
    _size = (2, 2)

    _target = None
    _damage = 1
    _speed = 1

    _state = NEW

    def __init__(self, position, target, damage):
        self._position = position
        self._target = target
        self._damage = damage

    def draw(self, screen):
        pass

    def update(self):
        pass
