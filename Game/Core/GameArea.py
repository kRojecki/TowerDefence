from Game.Utils.Constant import Position
from Game.Objects.Tile.TurretTile import TurretTile
from Game.Core.Event.Handler.GameAreaHandler import GameAreaHandler
from Game.Core.Calculator.NearestEnemyPositionCalculator import NearestEnemyPositionCalculator
from pygame import Surface
from Game.Objects.Enemy.RoundEnemy import RoundEnemy
from Game.Core.Initializer.DummyGameAreaInitializer import DummyGameAreaInitializer
from Game.Core.Initializer.Dto.GameAreaInitializerDTO import GameAreaInitializerDTO
from Game.Core.Collection.EnemyCollection import EnemyCollection
from Game.Core.Collection.BulletCollection import BulletCollection


class GameArea:

    # services
    _configuration = 0
    _nearest_enemy_calculator = 0

    # class attributes
    _screen = Surface((100, 100))
    _game_area = []
    _enemies = EnemyCollection([])
    _bullets = BulletCollection([])
    _game_area_margin = (0, 0)  # should be changed because of adding separated surface for gameArea

    # test fields only
    _game_area_dimension = [9, 18]  # to be removed when file based levels are implemented

    def __init__(self, configuration):
        self._configuration = configuration
        self._nearest_enemy_calculator = NearestEnemyPositionCalculator()

    def init(self):
        self._init_game_area()
        self._init_enemy()
        self._screen = Surface(self._calculate_surface_size())

        GameAreaHandler.register_object(self)

    def update(self):
        for fieldRow in self._game_area:
            for field in fieldRow:
                field.update(self._nearest_enemy_calculator.calculate(field, self._enemies))
        pass

        self._enemies.update()
        self._bullets.update()

    def draw(self, main_screen):
        self._screen.fill((5, 5, 5))
        self._draw_fields()
        self._enemies.draw(self._screen)
        self._bullets.draw(self._screen)

        main_screen.blit(self._screen, self._game_area_margin)

    def change_field(self, position, new_field):
        self._game_area[position[Position.X]][position[Position.Y]] = new_field

    def get_game_area(self):
        return self._game_area

    def _init_enemy(self):
        self._enemies.append(RoundEnemy())

    def _init_game_area(self):
        field_size = self._configuration.getint('GAME', 'field.size')
        dto = GameAreaInitializerDTO(self._game_area, field_size, self._game_area_dimension)

        game_initializer = DummyGameAreaInitializer()
        self._game_area = game_initializer.init_game_area(dto)

    def _draw_fields(self):
        for fieldRow in self._game_area:
            for field in fieldRow:
                if not isinstance(field, TurretTile):
                    self._draw_single_field(field)

        for fieldRow in self._game_area:
            for field in fieldRow:
                if isinstance(field, TurretTile):
                    self._draw_single_field(field)

    def _draw_single_field(self, field):
        field.draw(self._screen)

    def _calculate_surface_size(self):
        field_size = self._configuration.getint('GAME', 'field.size')
        return (
            len(self._game_area[0]) * field_size,
            len(self._game_area) * field_size
        )


