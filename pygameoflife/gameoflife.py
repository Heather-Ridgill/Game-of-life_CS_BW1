# import pygame
# start drawing
from datetime import datetime
import sys
import pygame
import pygame.draw
import random
import time
import tkinter as tk
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect



BOARD_SIZE = width, height = 840, 620
BOX_SIZE = 11
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 255, 0, 0
#FPS = Frames per sec, how fast does the grid move randomly?
MAX_FPS = 20
font = ('Arial Bold', 14)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)


gameDisplay = pygame.display.set_mode((BOARD_SIZE))
pygame.display.set_caption('Welcome to GAME OF LIFE!')
clock = pygame.time.Clock()

class GameOfLife:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.clear_screen()
        # flip = draw
        pygame.display.flip()

        self.last_update_completed = 0
        self.desired_milliseconds_between_updates = (1.0 / MAX_FPS) * 1000.0

        self.game_grid_active = 0       
        self.grids = []
        self.num_cols = int(width / BOX_SIZE)
        self.num_rows = int(height / BOX_SIZE)
        self.init_grids()
        self.set_grid()
        self.paused = False
        self.game_over = False


    def init_grids(self):
        
        def create_grid():
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0] * self.num_cols
                rows.append(list_of_columns)
            return rows
            
        self.grids.append(create_grid())
        self.grids.append(create_grid())

    # set_grid(0) all dead
    # set_grid(1) all alive
    # set_grid() Random
    # set_grid() Random
    def set_grid(self, value=None, grid = 0):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if value is None:
                    cell_value = random.randint(0, 1)
                else:
                    cell_value = value
                self.grids[grid][r][c] = cell_value
             
    def draw_grid(self):
        self.clear_screen()
        def text_objects (text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()

        def button(msg,x,y,w,h,ic,ac, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            else:
                pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

            smallText = pygame.font.SysFont('arial',20)
            textSurf, textRect = text_objects(msg, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            gameDisplay.blit(textSurf, textRect)

       
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                if self.grids[self.game_grid_active][r][c] == 1:
                    color = ALIVE_COLOR
                else:
                    color = DEAD_COLOR

                pygame.draw.rect(self.screen, color, (int(c*BOX_SIZE +(BOX_SIZE/2)), int(r*BOX_SIZE+(BOX_SIZE/2)), int(BOX_SIZE/2), int(BOX_SIZE/2)), 0)


        pygame.draw.rect(self.screen, red, (100, 25, 600, 45))
        largeText = pygame.font.Font("freesansbold.ttf", 40)
        textSurf, textRect = text_objects ("Welcome to...GAME OF LIFE!", largeText)
        textRect.center = ( (100+(600/2)),  (25+(45/2)) )
        self.screen.blit(textSurf, textRect)


        button (" 'P' = Pause", 75, 550, 110, 55, red, bright_red, "pause")
        button (" 'R' = Random", 375, 550, 110, 55, red, bright_red, "pause")
        button (" 'Q' = Quit", 675, 550, 110, 55, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(15)

        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill(DEAD_COLOR)

    def get_cell(self, r, c):
        try:
            cell_value = self.grids[self.game_grid_active][r][c]
        except:
            cell_value = 0
        return cell_value
    
    
    def check_cell_neighbors(self, row_index, col_index):
        # Get the number of alive cells surrounding current cell
        # implent the 4 rules: too populated, underpopulated, death, birth
        #check all 8 neighbors, add up alive count

        num_alive_neighbors = 0
        num_alive_neighbors += self.get_cell(row_index - 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index + 1)


        # RULES

        if self.grids[self.game_grid_active][row_index][col_index] == 1: #alive
            if num_alive_neighbors > 3: # 2.) Overpopulation
                return 0
            if num_alive_neighbors < 2: # 3.) Underpopulation
                return 0
            if num_alive_neighbors == 2 or num_alive_neighbors == 3:
                return 1
        elif self.grids[self.game_grid_active][row_index][col_index] == 0: # dead
            if  num_alive_neighbors == 3:
                return 1 # 4.) Come to life

        return self.grids[self.game_grid_active][row_index][col_index]


    def update_generation(self):
        # Inspect the current active
        self.set_grid(0, self.inactive_grid())
        for r in range(self.num_rows - 1):
            for c in range(self.num_cols - 1):
              next_gen_state = self.check_cell_neighbors(r, c)
              # Set the inactive grid future cell state
              self.grids[self.inactive_grid()][r][c] = next_gen_state
      
        # Update the inactive grid to store the next gen
        # swap out the active grid
        self.game_grid_active = self.inactive_grid()

        # self.set_grid(None)
        self.clear_screen()

    def inactive_grid(self):
        return (self.game_grid_active + 1) % 2
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'p':
                    print("Toggling pause")
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif event.unicode == 'r':
                        print("Randomizing grid")
                        self.game_grid_active = 0
                        self.set_grid(None, self.game_grid_active) #Randomize
                        self.set_grid(0, self.inactive_grid()) #Set to 0
                        self.draw_grid()
                elif event.unicode == 'q':
                        print("Exiting...")
                        self.game_over = True
            if event.type == pygame.QUIT: 
                sys.exit()  
# Game Loop Below from pygame website "how-to" docs
    def run(self):
        """
        Kick off the game and loop forever until quit state.
        """
        while True:
          if self.game_over: 
            return 

          self.handle_events() 
          if self.paused:
              continue

          self.update_generation()
          self.draw_grid()

          self.cap_frame_rate()
          



    def cap_frame_rate(self):
        """
        If game is running too fast and updating frames too frequently, just wait to maintin stable framrate
        """
        now = pygame.time.get_ticks()
        milliseconds_since_last_update = now - self.last_update_completed

        time_to_sleep = self.desired_milliseconds_between_updates - milliseconds_since_last_update
        if time_to_sleep > 0:
              pygame.time.delay(int(time_to_sleep))
        self.last_update_completed = now



if __name__ == "__main__":
    """
    Launch a game of life!
    """
    game = GameOfLife()
    game.run()


