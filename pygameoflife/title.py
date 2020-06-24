import sys
import pygame
import pygame.draw
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,200,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Welcome to.... GAME OF LIFE!!')
clock = pygame.time.Clock()


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.tff, 115')
        TextSurf, TextRect = text_objects('Welcome to.... GAME OF LIFE!!', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gameDisplay, green, (150,450,100,50))


        

