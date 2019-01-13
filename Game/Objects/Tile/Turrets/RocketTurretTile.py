from Game.Objects.Tile.Turrets.TurretTile import TurretTile
import pygame
from Game.Utils.Constant import Position
from pygame import Surface
from Game.Objects.Bullet.Enum.BulletEnum import BulletEnum


class RocketTurretTile(TurretTile):

    _range = 150
    _fire_rate = 2

    _bullet_type = BulletEnum.ROCKET_INSTANT_BULLET

    def draw_cannon(self):
        cannon = Surface(self._size, pygame.SRCALPHA)
        cannon_rect = pygame.Rect(
            self._size[Position.X] / 4,
            self._size[Position.Y] / 16,
            25,
            35
        )
        pygame.draw.rect(
            cannon,
            self._border_color,
            cannon_rect,
            0
        )

        #self._draw_range_circle(cannon)

        return cannon
