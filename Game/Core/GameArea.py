from Utils.Constant import Position
from Game.Objects.Tile.EmptyTile import EmptyTile
from pygame import Surface


class GameArea:

    configuration = 0
    screen = Surface((100,100))
    game_area = []
    field_size = 10
    game_area_margin = (0, 0) # should be changed because of adding separated surface for gameArea
    game_area_dimesions = [9, 18]

    def __init__(self, configuration):
        self.configuration = configuration
        self.screen = Surface((1000, 600))

    def init(self):
        self.field_size = self.configuration.getint('GAME', 'field.size')
        self.init_fields()

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

    def update(self, main_screen):
        self.screen.fill((5, 5, 5))
        self.check_events()
        self.draw_fields()

        main_screen.blit(self.screen, self.game_area_margin)

    def change_field(self, position, new_field):
        self.game_area[position[Position.X]][position[Position.Y]] = new_field

    def draw_fields(self):
        for fieldRow in self.game_area:
            for field in fieldRow:
                self.draw_single_field(field)

    def draw_single_field(self, field):
        field.draw(self.screen)

    def check_events(self):
        pass