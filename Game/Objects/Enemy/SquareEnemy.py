from Game.Objects.Enemy.Enemy import Enemy
import pygame
from Utils.Constant import Color, Position


class SquareEnemy(Enemy):

    _size = (10, 10)
    _speed = 0.15
    _health = 200

    def draw(self, screen):
        rect = pygame.Rect(
            self.get_position()[Position.X],
            self.get_position()[Position.Y],
            self.get_size()[Position.X],
            self.get_size()[Position.Y],
        )
        pygame.draw.rect(screen, Color.RED, rect, 2)
