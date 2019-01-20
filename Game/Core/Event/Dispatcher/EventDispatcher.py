import pygame


class EventDispatcher:

    @staticmethod
    def dispatch(event_type, sub_event_type, arguments):
        sub_event = {"sub_event": sub_event_type}
        pygame.event.post(
            pygame.event.Event(
                event_type,
                dict(arguments, **sub_event)
            )
        )
