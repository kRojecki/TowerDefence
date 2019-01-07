from Game.Utils.Constant import Position
from Game.Objects.Tile.EmptyTile import EmptyTile
from Game.Objects.Tile.TurretTile import TurretTile
from Game.Core.Handler.GameAreaHandler import GameAreaHandler
from Game.Core.Calculator.NearestEnemyPositionCalculator import NearestEnemyPositionCalculator
from pygame import Surface
from Game.Objects.Enemy.Enemy import Enemy


class GameArea:

    configuration = 0
    screen = Surface((100, 100))
    game_area = []
    _enemy = []
    start_point = [0,5]
    field_size = 10
    game_area_margin = (0, 0) # should be changed because of adding separated surface for gameArea
    game_area_dimesions = [9, 18]

    _nearest_enemy_calculator = 0

    def __init__(self, configuration):
        self.configuration = configuration
        self.screen = Surface((1000, 600))
        self._nearest_enemy_calculator = NearestEnemyPositionCalculator()

    def init(self):
        self.field_size = self.configuration.getint('GAME', 'field.size')
        self.init_fields()
        self.init_enemy()
        GameAreaHandler.register_object(self)

    def init_fields(self):
        row = 0
        column = 0
        for areaRow in range(self.game_area_dimesions[Position.X]):
            new_row = []
            for field in range(self.game_area_dimesions[Position.Y]):
                new_row.append(EmptyTile([column, row], self.field_size, self.game_area_margin))
                row += 1
            column += 1
            row = 0
            self.game_area.append(new_row)

    def init_enemy(self):
        self._enemy.append(Enemy());

    def update(self):
        for fieldRow in self.game_area:
            for field in fieldRow:
                field.update(self._nearest_enemy_calculator.calculate(field, self._enemy))
        pass

        for enemy in self._enemy:
            enemy.update()

    def change_field(self, position, new_field):
        self.game_area[position[Position.X]][position[Position.Y]] = new_field

    def draw_fields(self):
        for fieldRow in self.game_area:
            for field in fieldRow:
                if isinstance(field, EmptyTile):
                    self.draw_single_field(field)

        for fieldRow in self.game_area:
            for field in fieldRow:
                if isinstance(field, TurretTile):
                    self.draw_single_field(field)

    def draw_single_field(self, field):
        field.draw(self.screen)

    def draw_enemies(self):
        for enemy in self._enemy:
            enemy.draw(self.screen)

    def draw(self, main_screen):
        self.screen.fill((5, 5, 5))
        self.draw_fields()
        self.draw_enemies()

        main_screen.blit(self.screen, self.game_area_margin)

    def get_game_area(self):
        return self.game_area

