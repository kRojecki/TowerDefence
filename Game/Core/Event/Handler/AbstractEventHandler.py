class AbstractEventHandler:

    @classmethod
    def handle(cls, event) -> None:
        method_name = getattr(cls, event.sub_event)
        method_name(event)
