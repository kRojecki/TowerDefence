import pygame
import math
from Utils.Constant import Position
from Game.Objects.EmptyTile import EmptyTile
from Game.Objects.TurretTile import TurretTile
from pygame import Surface


class GameArea:

    screen = Surface((100,100))
    game_area = []
    field_size = 50
    game_area_margin = [10, 10] # should be changed because of adding separated surface for gameArea
    game_area_dimesions = [9, 18]

    def __init__(self):
        self.screen = Surface((1000, 600))
        pass

    def init_field(self):
        row = 0
        column = 0
        for areaRow in range(self.game_area_dimesions[Position.X]):
            newRow = []
            for field in range(self.game_area_dimesions[Position.Y]):
                newRow.append(EmptyTile([column, row]))
                row += 1
            column += 1
            row = 0
            self.game_area.append(newRow)

    def update(self):
        self.screen.fill((5,5,5))
        selected_field = self.get_selected_field()
        self.draw_fields(selected_field)
        return self.screen

    def change_field(self, position, new_field):
        self.game_area[position[Position.X]][position[Position.Y]] = new_field

    def draw_fields(self, selected_field):
        for fieldRow in self.game_area:
            for field in fieldRow:
                self.draw_single_field(field, selected_field)

    def draw_single_field(self, field, selected):
        field.draw(self.screen)
        mouse_pressed_buttons = pygame.mouse.get_pressed()

        if selected[Position.X] == field.get_tile_position()[Position.X] and selected[Position.Y] == field.get_tile_position()[Position.Y]:
            if(mouse_pressed_buttons[0] == 1):
                self.game_area[selected[Position.X]][selected[Position.Y]] = TurretTile(field.get_tile_position())
            if (mouse_pressed_buttons[2] == 1):
                self.game_area[selected[Position.X]][selected[Position.Y]] = EmptyTile(field.get_tile_position())

    # Rewrite and move calculate logic from here, after adding additional surface
    # Fails when gameAreaMargin or game surface will be changed
    def get_selected_field(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed_buttons = pygame.mouse.get_pressed()

        x = math.floor((mouse_pos[Position.Y] - self.game_area_margin[Position.X]) / self.field_size)
        y = math.floor((mouse_pos[Position.X] - self.game_area_margin[Position.Y]) / self.field_size)

        # Protects from click outside of game area
        x = x if x <= self.game_area_dimesions[Position.X] - 1 else -1
        y = y if y <= self.game_area_dimesions[Position.Y] - 1 else -1

        if (x != -1 and y != -1 and mouse_pressed_buttons[0] == 1):
            print(self.game_area[x][y].get_rect_position());

        return [x, y];
