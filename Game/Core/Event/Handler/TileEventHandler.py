class TileEventHandler:

    @staticmethod
    def handle(event):
        method_name = getattr(TileEventHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def _turret_upgrade(event):
        pass


