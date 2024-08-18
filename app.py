import pygame
import sys
from player import Player
from cloud import Cloud
from camera import Camera
from block import Block
from tube import Tube
from mountain import Mountain
from big_mountain import Big_Mountain
from bush import Bush
from bush import Small_Bush

pygame.init()

SCREEN_HEIGHT = 32*14
SCREEN_WIDTH = 32*25
FPS = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Bros. Remake")


all_sprites = pygame.sprite.Group()
# Initialize Pygame
clouds = pygame.sprite.Group()

clock = pygame.time.Clock()
# Main game loop
running = True

blocks = pygame.sprite.Group()
tubes = pygame.sprite.Group()
mountains = pygame.sprite.Group()
bushes = pygame.sprite.Group()

level_map = [
    "                                                                   ",
    "      C                                C                           ",
    "             C                                                     ",
    "                                                                   ",
    "                                                                   ",
    "                                                                   ",
    "                                                                   ",
    "                                                                   ",
    "M                                    T                             ",
    "               M            T                                      ",
    "           B           b                                           ",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
]

camera = Camera(len(level_map[0]) * 32, len(level_map) * 32, SCREEN_WIDTH, SCREEN_HEIGHT)
for row_index,row in enumerate(level_map):
    for col_index, col in enumerate(row):
        if col == 'G':
            block = Block(col_index*32, row_index*32)
            blocks.add(block)

        elif col == 'C':
            print(col_index, row_index)
            cloud = Cloud(col_index*32, row_index*32)
            clouds.add(cloud)

        elif col == 'T':
            tube = Tube(col_index*32, row_index*32)
            tubes.add(tube)

        elif col == 'm':
            mountain = Mountain(col_index*32, row_index*32)
            mountains.add(mountain)

        elif col == 'M':
            mountain = Big_Mountain(col_index*32, row_index*32)
            mountains.add(mountain)
        
        elif col == 'B':
            bush = Bush(col_index*32, row_index*32)
            bushes.add(bush)

        elif col == 'b':
            bush = Small_Bush(col_index*32, row_index*32)
            mountains.add(bush)

player = Player(100, SCREEN_HEIGHT - 4 * 32 , blocks= blocks , tubes=tubes)
# Set up display
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    camera.update(player)

    # Draw everything
    screen.fill((0, 140, 250)) 

    for mountain in mountains:
        screen.blit(mountain.image, camera.apply(mountain))

    for tube in tubes:
        screen.blit(tube.image, camera.apply(tube))

    for block in blocks:
        screen.blit(block.image, camera.apply(block))

    for cloud in clouds:
        screen.blit(cloud.image, camera.apply(cloud))

    for bush in bushes:
        screen.blit(bush.image, camera.apply(bush))

    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))
    

    pygame.display.flip()  # Update the display
    clock.tick(FPS)

pygame.quit()
sys.exit()
