from Game.Utils.Constant import Position
from Game.Core.Initializer.GameAreaInitializer import GameAreaInitializer
from Game.Core.Factory.TileFactory import TileFactory


class DummyGameAreaInitializer(GameAreaInitializer):

    def init_game_area(self, dto):
        game_area = dto.game_area

        row = 0
        column = 0
        for areaRow in range(dto.game_area_dimesions[Position.X]):
            new_row = []
            for field in range(dto.game_area_dimesions[Position.Y]):
                new_row.append(TileFactory.create_tile_from_args([column, row], dto.field_size, 'EmptyTile'))
                row += 1
            column += 1
            row = 0
            game_area.append(new_row)

        return game_area
