from Game.Objects.Tile.Tile import Tile
import pygame
from Game.Utils.Constant import Color, Position, PointableState, EventEnum
from pygame import Surface
from Game.Core.Calculator.Tile.TileRotationCalculator import TileRotationCalculator
from Game.Core.Calculator.Tile.TileDistanceCalculator import TileDistanceCalculator
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher


from Game.Utils.Helper.TransformHelper.RotationHelper import RotationHelper


class TurretTile(Tile):
    _border_color = (200, 90, 90)
    _background_color = {
        PointableState.CLEAR: (100, 10, 10),
        PointableState.HOVER: Color.GRAY,
        PointableState.CLICKED: Color.WHITE
    }

    _rotation = -90
    _range = 250
    _bullet = 0
    _fire_rate = 1

    _fire_rate_clock = 0

    def _draw_border(self, screen):
        super()._draw_border(screen)
        second_border_rect = (self._position[Position.X] + 2, self._position[Position.Y] + 2,
                              self._size[Position.X] - 3, self._size[Position.Y] - 3)

        pygame.draw.rect(screen, self._border_color, second_border_rect, 1)
        pygame.draw.circle(screen, Color.GRAY, self.get_center(), self._range, 1)

    def update(self, nearest_enemy):

        if self._range > TileDistanceCalculator.calculate_distance(self, nearest_enemy):
            self._rotation = TileRotationCalculator.calculate_rotation(self, nearest_enemy)

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
            self._border_color,
            cannon_points,
            0
        )

        # temporary to show circle fire area
        pygame.draw.circle(
            cannon,
            self._border_color,
            (int(self._size[Position.X] / 2), int(self._size[Position.Y] / 10)),
            3,
            1
        )

        return cannon

    def _fire_to(self, nearest_enemy):
        EventDispatcher.dispatch(
            EventEnum.FIRE,
            {
                "turret": self,
                "enemy": nearest_enemy,
                "start_position": ((self._size[Position.X] / 2), self._size[Position.Y] / 10),
            }
        )
