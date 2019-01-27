from Game.Core.Factory.TileFactory import TileFactory
from Game.Utils.Helper.ClassProvider import ClassProvider


class TileMapper:

    DEFAULT = 'Resources.Data.TileMap.Default.Default'

    _definition = None
    _map = None

    def __init__(self, definition=DEFAULT):
        self._definition = ClassProvider.provide_class(definition)
        self._map = self._definition.MAP

    def map(self, value, tile_position, size):
        return TileFactory.create_tile_from_args(tile_position, size, self._map_field(value))

    def _map_field(self, value):
        if value in self._map:
            return self._map[value]

        raise Exception('Field type ' + value + ' has no mapping in ' + self._definition.__module__)




