from Game.Core.Mapper.TileMapper import TileMapper


class FileMapParser:

    MAP_BEGIN_TAG = '## MAP BEGIN ##'
    MAP_END_TAG = '## MAP END ##'

    SEPARATOR = ' '

    NONE = 0
    MAP = 1
    DATA = 2

    _tile_mapper = None

    _parsing_state = NONE
    _map = []
    _field_size = ()

    def __init__(self, field_size):
        self._tile_mapper = TileMapper()
        self._field_size = field_size

    def parse(self, file_lines):

        for line in file_lines:

            if line == self.MAP_BEGIN_TAG:
                self._parsing_state = self.MAP
                continue

            if self._parsing_state == self.MAP and line == self.MAP_END_TAG:
                self._parsing_state = self.NONE

            if self._parsing_state == self.MAP and line != self.MAP_END_TAG:
                fields = line.split(self.SEPARATOR)
                row = []
                for field in fields:
                    row.append(
                        self._tile_mapper.map(
                            field,
                            (len(self._map), len(row)),
                            self._field_size
                        )
                    )
                self._map.append(row)

        return self._map
