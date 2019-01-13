from Game.Utils.Constant import Position
from Game.Objects.Tile.EmptyTile import EmptyTile
from Game.Core.Event.Handler.GameAreaHandler import GameAreaHandler
from Game.Core.Event.Handler.BulletHandler import BulletHandler
from Game.Core.Event.Handler.EnemyHandler import EnemyHandler
from Game.Core.Calculator.NearestEnemyPositionCalculator import NearestEnemyPositionCalculator
from pygame import Surface
from Game.Objects.Enemy.RoundEnemy import RoundEnemy
from Game.Core.Initializer.FileBasedLevelGameAreaInitializer import FileBasedLevelGameAreaInitializer
from Game.Core.Initializer.Dto.GameAreaInitializerDTO import GameAreaInitializerDTO
from Game.Core.Collection.EnemyCollection import EnemyCollection
from Game.Core.Collection.BulletCollection import BulletCollection


class GameArea:

    # services
    _configuration = None
    _nearest_enemy_calculator = None

    # class attributes
    _screen = None
    _game_area = []
    _enemies = EnemyCollection()
    _bullets = BulletCollection()
    _game_area_margin = (0, 0)  # should be changed because of adding separated surface for gameArea

    def __init__(self, configuration):
        self._configuration = configuration
        self._nearest_enemy_calculator = NearestEnemyPositionCalculator(self._enemies)

    def init(self):
        self._init_game_area()
        self._init_enemy()
        self._screen = Surface(self._calculate_surface_size())

        GameAreaHandler.register_object(self)
        BulletHandler.register_object(self._bullets)
        EnemyHandler.register_object(self._enemies)

    def update(self):
        for fieldRow in self._game_area:
            for field in fieldRow:
                field.update(self._nearest_enemy_calculator.calculate(field))

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
        dto = GameAreaInitializerDTO(field_size, 'Resources/levels/level1.dat')

        game_initializer = FileBasedLevelGameAreaInitializer()
        self._game_area = game_initializer.init_game_area(dto)

    def _draw_fields(self):
        for fieldRow in self._game_area:
            for field in fieldRow:
                if isinstance(field, EmptyTile):
                    self._draw_single_field(field)

        for fieldRow in self._game_area:
            for field in fieldRow:
                if not isinstance(field, EmptyTile):
                    self._draw_single_field(field)

    def _draw_single_field(self, field):
        field.draw(self._screen)

    def _calculate_surface_size(self):
        field_size = self._configuration.getint('GAME', 'field.size')
        return (
            len(self._game_area[Position.X]) * field_size,
            len(self._game_area) * field_size
        )


