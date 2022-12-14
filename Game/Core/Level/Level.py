from pygame import Surface

from Configuration.General.Configuration import Configuration
from Core.Initializer.Level.Dto.GameAreaInitializerDTO import GameAreaInitializerDTO
from Core.Initializer.Level.FileBasedLevelGameAreaInitializer import FileBasedLevelGameAreaInitializer
from Game.Core.Calculator.NearestEnemyPositionCalculator import NearestEnemyPositionCalculator
from Game.Core.Collection.BulletCollection import BulletCollection
from Game.Core.Collection.EnemyCollection import EnemyCollection
from Game.Core.Event.Handler.BulletEventHandler import BulletEventHandler
from Game.Core.Event.Handler.EnemyEventHandler import EnemyEventHandler
from Game.Core.Event.Handler.LevelEventHandler import LevelEventHandler
from Game.Objects.Tile.Turrets.TurretTile import TurretTile
from Game.Utils.Constant import Position
from Utils.Constant import Color


class Level:
    # services
    _nearest_enemy_calculator = None

    # class attributes
    _screen = None
    _game_area = []

    _enemies = EnemyCollection()
    _bullets = BulletCollection()

    _path = None

    area_size = (0, 0)

    _game_area_margin = (0, 0)  # should be changed because of adding separated surface for gameArea

    def __init__(self):
        self._nearest_enemy_calculator = NearestEnemyPositionCalculator(self._enemies)

    def init(self):
        self._init_game_area()
        Level.area_size = self._calculate_surface_size()
        self._screen = Surface(Level.area_size)

        LevelEventHandler.register_object(self)
        BulletEventHandler.register_object(self._bullets)
        EnemyEventHandler.register_object(self._enemies)
        EnemyEventHandler.set_enemy_path(self._path)

    def _init_game_area(self):
        field_size = Configuration.get_int('GAME', 'field.size')
        dto = GameAreaInitializerDTO(field_size, Configuration.get_str('GAME', 'level.first'))

        game_initializer = FileBasedLevelGameAreaInitializer()
        self._game_area = game_initializer.init_game_area(dto)
        self._path = game_initializer.prepare_map_path(self._game_area)

    def update(self):
        for fieldRow in self._game_area:
            for field in fieldRow:
                field.update(self._nearest_enemy_calculator.calculate(field))

        self._enemies.update()
        self._bullets.update()

    def draw(self, main_screen):
        self._screen.fill(Color.DARK_GRAY)

        self._draw_fields()
        self._enemies.draw(self._screen)
        self._bullets.draw(self._screen)

        main_screen.blit(self._screen, self._game_area_margin)

    def _draw_fields(self):
        for fieldRow in self._game_area:
            for field in fieldRow:
                if not isinstance(field, TurretTile):
                    field.draw(self._screen)

        for fieldRow in self._game_area:
            for field in fieldRow:
                if isinstance(field, TurretTile):
                    field.draw(self._screen)

    def change_field(self, position, new_field):
        self._game_area[position[Position.Y]][position[Position.X]] = new_field

    def _calculate_surface_size(self):
        field_size = Configuration.get_int('GAME', 'field.size')
        return (
            len(self._game_area[Position.X]) * field_size,
            len(self._game_area) * field_size
        )

