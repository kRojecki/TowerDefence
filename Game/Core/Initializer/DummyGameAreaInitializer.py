from Game.Utils.Constant import Position
from Game.Core.Initializer.GameAreaInitializer import GameAreaInitializer
from Game.Core.Factory.TileFactory import TileFactory
from Game.Objects.Tile.Enum.TileEnum import TileEnum

class DummyGameAreaInitializer(GameAreaInitializer):

    # test fields only
    _game_area_dimension = [9, 18]  # to be removed when file based levels are implemented

    def init_game_area(self, dto):
        game_area = []

        row = 0
        column = 0
        for areaRow in range(self._game_area_dimension[Position.X]):
            new_row = []
            for field in range(self._game_area_dimension[Position.Y]):
                new_row.append(TileFactory.create_tile_from_args([column, row], dto.field_size, TileEnum.EMPTY_TILE))
                row += 1
            column += 1
            row = 0
            game_area.append(new_row)

        return game_area
