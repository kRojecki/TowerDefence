import pygame
from Objects.Abstracts.Hoverable import Hoverable


class Clickable(Hoverable):

    def on_click(self, mouse_position):
        pressed = pygame.mouse.get_pressed()
        if self._is_hover(mouse_position) and pressed != (0, 0, 0):
            self._click_action(pressed)

    def _click_action(self, pressed):
        pass
