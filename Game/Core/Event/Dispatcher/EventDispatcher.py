import pygame


class EventDispatcher:

    @staticmethod
    def dispatch(event_type, arguments):
        pygame.event.post(
            pygame.event.Event(
                event_type,
                arguments
            )
        )
