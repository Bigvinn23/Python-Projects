# This will be a basic game of Snake made using the pygame module

import pygame
import os

main_dir = os.path.dirname(os.path.abspath(__file__)) + '/../' # get the parent directory

# ===========================SPRITES========================== #

class Apple(pygame.sprite.Sprite):
    def __init__(self, position = (0, 0)):
        super().__init__()
        self.image = pygame.image.load(main_dir + 'images/apple.png').convert_alpha()
        self.rect = self.image.get_rect(center = position)

class WallSegment(pygame.sprite.Sprite):
    def __init__(self, type, position = (0, 0), rotation = 0):
        super().__init__()

        # type == 1 is a straight piece, 2 is a corner
        self.image = pygame.image.load(main_dir + 'images/Border' + str(type) + '.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(center = position)

class Controls(pygame.sprite.Sprite):
    def __init__(self, position = (0, 0)):
        super().__init__()

        self.image = pygame.image.load(main_dir + 'images/Arrows1.png').convert_alpha()
        self.rect = self.image.get_rect(center = position)
    
    def show_controls(self, next_move):
        keys = pygame.key.get_pressed()

        if next_move == pygame.K_UP:
            self.image = pygame.image.load(main_dir + 'images/Arrows2.png').convert_alpha()
        elif next_move == pygame.K_DOWN:
            self.image = pygame.transform.rotate(pygame.image.load(main_dir + 'images/Arrows2.png').convert_alpha(), 180)
        elif next_move == pygame.K_LEFT:
            self.image = pygame.transform.rotate(pygame.image.load(main_dir + 'images/Arrows2.png').convert_alpha(), 90)
        elif next_move == pygame.K_RIGHT:
            self.image = pygame.transform.rotate(pygame.image.load(main_dir + 'images/Arrows2.png').convert_alpha(), 270)

    def update(self, next_move):
        self.show_controls(next_move)

# Sprites for the Player
class SnakeSegment(pygame.sprite.Sprite):
    # static dictionary of all snake body parts
    body_parts = {
        "straight" : pygame.image.load(main_dir + 'images/Snake3.png'),
        "turn" : pygame.image.load(main_dir + 'images/Snake4.png'),
        "tail" : pygame.image.load(main_dir + 'images/Snake2.png')
    }

    def __init__(self, position, rotation = 0, type = "straight"):
        super().__init__()

        self.image = pygame.transform.rotate(self.body_parts[type].convert_alpha(), rotation)
        self.rect = self.image.get_rect(center = position)

    def set_image(self, type, rotation):
        self.image = pygame.transform.rotate(self.body_parts[type].convert_alpha(), rotation)

class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, position, rotation = 0):
        super().__init__()

        # type == 1 is a straight piece, 2 is a corner
        self.image = pygame.image.load(main_dir + 'images/Snake1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(center = position)

    def set_image(self, rotation):
        self.image = pygame.image.load(main_dir + 'images/Snake1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, rotation)

# Class for the player, will handle snake construction and controls
class Player():
    # static sprite size variable
    SPRITE_SIZE = 16

    # static dictionary of conflicting movement directions
    conflicting_directions = {
        "down" : "up",
        "up" : "down",
        "left" : "right",
        "right" : "left"
    }

    # static dictionary of movement direction should change location tuples
    direction_changes = {
        "down" : (0, 1),
        "up" : (0, -1),
        "left" : (-1, 0),
        "right" : (1, 0)
    }

    # static dictionary of how "position difference" tuples map to sprite segment type and rotation
    position_diff = {
        (2, 0) : ["straight", 0],
        (0, 2) : ["straight", 90],
        (1, 1) : ["turn", 180],
        (-1, -1) : ["turn", 270],
        (-1, -1) : ["turn", ],
        (-1, -1) : ["turn", ],
    }

    def __init__(self, starting_position):
        # group for head
        self.snake_head = pygame.sprite.GroupSingle()
        self.snake_head.add(SnakeHead(starting_position))

        # group for body
        self.snake_body = pygame.sprite.Group()
        for i in range(1, 4):
            self.snake_body.add(SnakeSegment((starting_position[0], starting_position[1] - (i * 16))))
        
        # initialize facing direction and next direction
        self.facing_direction = "down"
        self.next_direction = "down"
        self.food = 0

    def draw_snake(self, surface):
        self.snake_head.draw(surface)
        self.snake_body.draw(surface)

    # handles the snake's movement, along with reassigning the images of the segments
    def update_snake(self):
        # UPDATE THE SNAKE'S POSITIONS
        # add segment if snake is full
        if self.food:
            self.snake_body.add(SnakeSegment((0, 0)))
            self.food -= 1

        # loop through the snake in reverse order to reassign the positions of each segment to the position of the one in front, essentially moving every segment forward one segment
        for i in range(1, len(self.snake_body)):
            self.snake_body.sprites()[-i].rect.center = self.snake_body.sprites()[-(i + 1)].rect.center
        
        # assign the first body segment to the position of the head
        self.snake_body.sprites()[0].rect.center = self.snake_head.sprite.rect.center

        # reassign the position of the head based on the next direction and if it doesnt conflict with the current direction
        if self.next_direction == self.conflicting_directions[self.facing_direction]:
            self.next_direction = self.facing_direction

        # change the position of the snake head based on how the next direction maps to direction_changes
        self.snake_head.sprite.rect.center = (self.snake_head.sprite.rect.centerx + (self.direction_changes[self.next_direction][0] * self.SPRITE_SIZE), self.snake_head.sprite.rect.centery + (self.direction_changes[self.next_direction][1] * self.SPRITE_SIZE))

        # UPDATE THE SNAKE'S IMAGES
        # change snake head's direction
        self.snake_head.sprite.set


# ==========================FUNCTIONS========================= #

# returns a group of border sprites around the edges of the provided rectangle
def create_borders(play_space_rect):
    play_space_borders = pygame.sprite.Group()

        # left border
    for i in range(1, int(play_space_rect.height / SPRITE_SIZE)):
        play_space_borders.add(WallSegment(1, (play_space_rect.left, play_space_rect.top + (i * SPRITE_SIZE))))

        # right border
    for i in range(1, int(play_space_rect.height / SPRITE_SIZE)):
        play_space_borders.add(WallSegment(1, (play_space_rect.right, play_space_rect.top + (i * SPRITE_SIZE)), 180))

        # top border
    for i in range(1, int(play_space_rect.height / SPRITE_SIZE)):
        play_space_borders.add(WallSegment(1, (play_space_rect.left + (i * SPRITE_SIZE), play_space_rect.top), 270))

        # bottom border
    for i in range(1, int(play_space_rect.height / SPRITE_SIZE)):
        play_space_borders.add(WallSegment(1, (play_space_rect.left + (i * SPRITE_SIZE), play_space_rect.bottom), 90))

        # corners
    play_space_borders.add(WallSegment(2, (play_space_rect.topleft)))
    play_space_borders.add(WallSegment(2, (play_space_rect.topright), 270))
    play_space_borders.add(WallSegment(2, (play_space_rect.bottomleft), 90))
    play_space_borders.add(WallSegment(2, (play_space_rect.bottomright), 180))

    return play_space_borders

pygame.init() # Initialize pygame

# Create Window
GAME_WIDTH = 650
GAME_HEIGHT = 500
screen = pygame.display.set_mode( (GAME_WIDTH, GAME_HEIGHT) )
clock = pygame.time.Clock()

# Title, Icon, Background
pygame.display.set_caption("Snake")
game_icon = pygame.image.load(main_dir + 'images/Snake1.png')
pygame.display.set_icon(game_icon)
bg_color = '#a4a4a4'
playe_space_color = '#a4eebb'

# =======================MISC. VARIABLES====================== #
SPRITE_SIZE = 16

# make rectangle to represent the play space
play_space_rect = pygame.Rect(10, 10, 480, 480)

next_move = 'down'

# ===========================GROUPS=========================== #
# Apple
apples = pygame.sprite.Group() # not sure if i will allow multiple apples at once so ill just make this a group

# for i in range(1, 30):
#     for j in range(1, 30):
#         apples.add(Apple(((i*16) + 10, (j*16) + 10)))

# Play space construction
play_space_borders = create_borders(play_space_rect)

# Controls
controls = pygame.sprite.GroupSingle()
controls.add(Controls((play_space_rect.right + ((GAME_WIDTH - play_space_rect.right) / 2), (GAME_WIDTH - play_space_rect.right) / 2) ))

# Player
player = Player((300, 200))

# Game Loop
while True:
    screen.fill(bg_color)

    # ===============EVENTS=============== #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                next_move = event.key
    
    # ==========DRAWING ELEMENTS========== #
    pygame.draw.rect(screen, playe_space_color, play_space_rect)
    play_space_borders.draw(screen)
    apples.draw(screen)

    controls.draw(screen)
    controls.update(next_move)

    player.draw_snake(screen)

    pygame.display.update()
    clock.tick(60)