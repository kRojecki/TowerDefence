import pygame
from Objects.Abstracts.Hoverable import Hoverable


class Clickable(Hoverable):

    def on_click(self, mouse_position, button_pressed):
        if self._is_hover(mouse_position) and button_pressed != (0, 0, 0):
            self._click_action(button_pressed)

    def _click_action(self, pressed):
        pass
