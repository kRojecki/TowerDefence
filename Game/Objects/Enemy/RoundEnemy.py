from Game.Objects.Enemy.Enemy import Enemy
import pygame

from Utils.Constant import Color


class RoundEnemy(Enemy):

    def draw(self, screen):
        super().draw(screen)
        center = int(self._size[0]/2)
        pygame.draw.circle(self._surface, Color.RED, (center, center), center, self._border_width)
        self.blit(screen)
