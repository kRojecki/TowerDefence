import pygame
from Game.Utils.Constant import Position


class Hoverable:

    _position = ()
    _size = ()
    _absolute_rect = ()

    def _is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(self._position, self._size)

        if rect.collidepoint(mouse_pos[Position.X], mouse_pos[Position.Y]):
            return True
        return False

    def on_hover(self):
        if self._is_hover():
            return self._hover_action()
        else:
            return self._lost_focus_action()


    def _hover_action(self):
        pass

    def _lost_focus_action(self):
        pass
