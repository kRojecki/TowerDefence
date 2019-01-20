from Game.Objects.Tile.Tile import Tile
import pygame
from Game.Utils.Constant import Color, Position, PointableState
from Game.Utils.Constant.EventEnum import EventEnum
from Game.Utils.Constant.SubEventEnum import SubEventEnum
from pygame import Surface
from Game.Core.Calculator.Tile.TileRotationCalculator import TileRotationCalculator
from Core.Calculator.CenterDistanceCalculator import CenterDistanceCalculator
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Objects.Bullet.Enum.BulletEnum import BulletEnum


from Game.Utils.Helper.TransformHelper.RotationHelper import RotationHelper


class TurretTile(Tile):
    _border_color = Color.T_TURRET_TILE_BORDER
    _background_color = {
        PointableState.CLEAR: Color.T_TURRET_TILE_BACKGROUND_CLEAR,
        PointableState.HOVER: Color.T_TURRET_TILE_BACKGROUND_HOVER,
        PointableState.CLICKED: Color.T_TURRET_TILE_BACKGROUND_CLICKED
    }
    _cannon_color = Color.DARK_GRAY;
    _range_border_color = Color.LIGHT_GRAY

    _turret_barrel_position = ()

    _rotation = -90
    _range = 75
    _bullet = 0
    _fire_rate = 5

    _fire_rate_clock = 0

    _bullet_type = BulletEnum.INSTANT_BULLET

    def _draw_border(self, screen):
        super()._draw_border(screen)
        second_border_rect = (self._position[Position.X] + 2, self._position[Position.Y] + 2,
                              self._size[Position.X] - 3, self._size[Position.Y] - 3)

        pygame.draw.rect(screen, self._border_color, second_border_rect, 1)

    def update(self, nearest_enemy=None):

        if nearest_enemy is None or nearest_enemy.get_state() == nearest_enemy.KILLED:
            return

        if self._range > CenterDistanceCalculator.calculate_distance(self.get_center(), nearest_enemy.get_center()):
            self._rotation = TileRotationCalculator.calculate_rotation(self, nearest_enemy)
            self._turret_barrel_position = TileRotationCalculator.calculate_barrel_position(self, self._rotation)

            if self._fire_rate_clock == 0:
                self._fire_to(nearest_enemy)

        self._fire_rate_clock = (self._fire_rate_clock + self._fire_rate) % 60

    def _draw_tile_content(self, screen):
        super()._draw_tile_content(screen)
        cannon = self.draw_cannon()

        rotation_dto = RotationHelper.rotate(cannon, self._rotation)

        blit_destination = (self._position[Position.X] - rotation_dto.position_modifier[Position.X],
                            self._position[Position.Y] - rotation_dto.position_modifier[Position.Y])
        screen.blit(rotation_dto.transformed_surface, blit_destination)

    def draw_cannon(self):
        cannon = Surface(self._size, pygame.SRCALPHA)
        cannon_points = [
            ((self._size[Position.X] / 2), self._size[Position.Y] / 10),
            (self._size[Position.X] / 5, (3.5 * self._size[Position.Y]) / 5),
            ((4 * self._size[Position.X]) / 5, (3.5 * self._size[Position.Y]) / 5),
        ]
        pygame.draw.polygon(
            cannon,
            self._cannon_color,
            cannon_points,
            0
        )

        #self._draw_range_circle(cannon)

        return cannon

    def _fire_to(self, nearest_enemy):
        EventDispatcher.dispatch(
            EventEnum.BULLET,
            SubEventEnum.FIRE,
            {
                "turret": self,
                "enemy": nearest_enemy,
                "start_position": self._turret_barrel_position,
                "bullet_type": self._bullet_type
            }
        )

    def _draw_range_circle(self, cannon):
        # temporary to show circle fire area
        pygame.draw.circle(
            cannon,
            self._border_color,
            (int(self._size[Position.X] / 2), int(self._size[Position.Y] / 10)),
            3,
            1
        )
