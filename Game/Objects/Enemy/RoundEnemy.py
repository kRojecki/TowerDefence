from Game.Objects.Enemy.Enemy import Enemy
import pygame

from Utils.Constant import Color


class RoundEnemy(Enemy):

    def draw(self, screen):
            pygame.draw.circle(screen, Color.RED, self.get_position(), self._size[0], 2)
