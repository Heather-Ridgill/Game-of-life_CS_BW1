# import pygame
# start drawing

import sys
import pygame
import pygame.draw
import random


BOARD_SIZE = width, height = 640, 480
BOX_SIZE = 10
speed = [2, 2]
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 255, 0, 0


class GameOfLife:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.clear_screen()
        # flip = draw
        pygame.display.flip()

        self.init_grids()

    def init_grids(self):
        self.num_cols = int(width / BOX_SIZE)
        self.num_rows = int(height / BOX_SIZE)
        
        self.grids = [
            [[0] * self.num_rows] * self.num_cols,
            [[0] * self.num_rows] * self.num_cols]
        self.game_grid_active = 0
        self.set_grid()
        print(self.grids[0])

        # self.game_grid_inactive = []

    # set_grid(0) all dead
    # set_grid(1) all alive
    # set_grid() Random
    # set_grid() Random
    def set_grid(self, value=None):
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                if value is None:
                    cell_value = random.choice([0, 1])
                else:
                    cell_value = value
                self.grids[self.game_grid_active][c][r] = random.choice([0, 1])

    def draw_grid(self):
        self.clear_screen()
        # rect_box = pygame.draw.rect(self.screen, ALIVE_COLOR, (50, 50, 10, 10), 2)
        # print(type(rect_box))
        # print(rect_box)
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                pygame.draw.rect(self.screen, ALIVE_COLOR, (int(c*BOX_SIZE +(BOX_SIZE/2)), int(r*BOX_SIZE+(BOX_SIZE/2)), int(BOX_SIZE/2), int(BOX_SIZE/2)), 0)
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill(DEAD_COLOR)

    def update_generation(self):
        # Inspect the current active
        # Update the inactive grid to store the next gen
        # swap out the active grid
        
        pass



    def handle_events(self):
        for event in pygame.event.get():
        # if event is keypress of "s" then toggle game pause
        # if event is keypress of "r" then randomize grid
        # if event is keypress of "q" then quit
            if event.type == pygame.QUIT: 
                sys.exit()  
# Game Loop
    def run(self):
        while True:
          self.handle_events()
          # Time checking?
          self.update_generation()
          self.draw_grid()                         




if __name__ == "__main__":

    game = GameOfLife()
    game.run()