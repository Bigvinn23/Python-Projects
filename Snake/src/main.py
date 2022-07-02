# This will be a basic game of Snake made using the pygame module

import pygame

pygame.init() # Initialize pygame

# Create Window
GAME_WIDTH = 800
GAME_HEIGHT = 600
screen = pygame.display.set_mode( (GAME_WIDTH, GAME_HEIGHT) )

# Title, Icon, Background
pygame.display.set_caption("Snake")
game_icon = pygame.image.load('Snake/images/Snake1.png')
pygame.display.set_icon(game_icon)
bg_color = (100, 100, 100)

# Basic Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill(bg_color)

    pygame.display.update()