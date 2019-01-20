import pygame

from Utils.Constant import Color


class Score:

    _font = None

    def __init__(self):
        self._font = pygame.font.SysFont("ubuntumono", 16)

    def draw(self, score):
        label = self._font.render("Score:" + str(score), 1, Color.ORANGE)
        return label
