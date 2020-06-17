# import pygame
# start drawing

import sys
import pygame
import pygame.draw


BOARD_SIZE = width, height = 640, 480
speed = [2, 2]
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 255, 0, 0


class GameOfLife:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)

    def run(self):
        rect_box = pygame.draw.rect(self.screen, ALIVE_COLOR, (50, 50, 10, 10), 2)
        print(type(rect_box))
        print(rect_box)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.screen.fill(DEAD_COLOR)

            # screen.blit(ball, ballrect)
            # flip = draw
            pygame.display.flip()


if __name__ == "__main__":

    game = GameOfLife()
    game.run()