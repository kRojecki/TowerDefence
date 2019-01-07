from Game.Objects.Tile.Tile import Tile
import pygame
from Game.Utils.Constant import Color, Position, PointableState, EventEnum
from pygame import Surface
import math

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

    def _draw_border(self, screen):
        super()._draw_border(screen)
        second_border_rect = (self._position[Position.X] + 2, self._position[Position.Y] + 2,
                              self._size[Position.X] - 3, self._size[Position.Y] - 3)

        pygame.draw.rect(screen, self._border_color, second_border_rect, 1)
        pygame.draw.circle(screen, Color.GRAY, self.get_center(), self._range, 1)

    def update(self, nearest_enemy):

        if self._range > self._calculate_distance(nearest_enemy):
            self._calculate_rotation(nearest_enemy)
            self._fire_to(nearest_enemy)
        pass

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
        pygame.draw.polygon(cannon, self._border_color, cannon_points, 0)

        # temporary to show circle fire area
        pygame.draw.circle(cannon, self._border_color, ((int) (self._size[Position.X] / 2), (int) (self._size[Position.Y] / 10)), 3, 1)

        return cannon

    def _calculate_rotation(self, nearest_enemy):
        rel_y = nearest_enemy.get_center()[Position.Y] - self.get_center()[Position.Y]
        rel_x = nearest_enemy.get_center()[Position.X] - self.get_center()[Position.X]

        self._rotation = ((180 / math.pi) * -math.atan2(rel_y, rel_x)) - 90

    def _calculate_distance(self, nearest_enemy):
        enemy_vector = pygame.Vector2(nearest_enemy.get_center())
        self_vector = pygame.Vector2(self.get_center())

        return enemy_vector.distance_to(self_vector)

    def _fire_to(self, nearest_enemy):
        pygame.event.post(
            pygame.event.Event(
                EventEnum.FIRE,
                {
                    "turret": self,
                    "enemy": nearest_enemy,
                    "start_position": ((self._size[Position.X] / 2), self._size[Position.Y] / 10),
                }
            )
        )
