class GameAreaInitializerDTO:

    game_area = 0
    field_size = 0
    game_area_dimesions = ()

    def __init__(self, game_area, field_size, game_area_dimensions):
        self.game_area = game_area
        self.field_size = field_size
        self.game_area_dimesions = game_area_dimensions
