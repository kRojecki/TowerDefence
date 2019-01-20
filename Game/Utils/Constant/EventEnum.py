import pygame


class EventEnum:
    _prefix = pygame.USEREVENT

    LEVEL = _prefix + 0
    ENEMY = _prefix + 1
    BULLET = _prefix + 2

    @staticmethod
    def get_allowed_events():
        return [
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP,
            pygame.QUIT,
            EventEnum.LEVEL,
            EventEnum.ENEMY,
            EventEnum.BULLET
        ]
