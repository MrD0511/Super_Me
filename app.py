import pygame
import sys
from player import Player
from cloud import Cloud
from camera import Camera
from ground_block import Ground_Block, Block, Treasure_Block
from tube import Tube
from mountain import Mountain
from big_mountain import Big_Mountain
from bush import Bush
from bush import Small_Bush
from cloud import Small_Cloud
from ground_block import handle_collisions

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

ground_blocks = pygame.sprite.Group()
blocks = pygame.sprite.Group()
treasure_blocks = pygame.sprite.Group()
tubes = pygame.sprite.Group()
mountains = pygame.sprite.Group()
bushes = pygame.sprite.Group()

level_map = [
    "                              C                                    ",
    "      C                                C          C                ",
    "                     C                                C            ",
    "          C                                                        ",
    "                      T                                            ",
    "                                                                   ",
    "                                                                   ",
    "                 T  lTlTl                                          ",
    "M                                    P                             ",
    "               M            P                                      ",
    "           B           b                                           ",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
]

camera = Camera(len(level_map[0]) * 32, len(level_map) * 32, SCREEN_WIDTH, SCREEN_HEIGHT)
for row_index,row in enumerate(level_map):
    for col_index, col in enumerate(row):
        if col == 'G':
            block = Ground_Block(col_index*32, row_index*32)
            ground_blocks.add(block)

        elif col == 'C':
            print(col_index, row_index)
            cloud = Small_Cloud(col_index*32, row_index*32)
            clouds.add(cloud)

        elif col == 'P':
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

        elif col == 'l':
            block = Block(col_index*32, row_index*32)
            blocks.add(block)

        elif col == 'T':
            block = Treasure_Block(col_index*32, row_index*32)
            treasure_blocks.add(block)


player = Player(100, SCREEN_HEIGHT - 4 * 32 , ground= ground_blocks , tubes=tubes)
# Set up display
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # blocks.update(player)
    # treasure_blocks.update(player)
    player.update(blocks=blocks)
    camera.update(player)

    # Draw everything
    screen.fill((0, 140, 250)) 

    for mountain in mountains:
        screen.blit(mountain.image, camera.apply(mountain))

    for tube in tubes:
        screen.blit(tube.image, camera.apply(tube))

    for block in ground_blocks:
        screen.blit(block.image, camera.apply(block))

    for cloud in clouds:
        screen.blit(cloud.image, camera.apply(cloud))

    for bush in bushes:
        screen.blit(bush.image, camera.apply(bush))

    for block in blocks:
        screen.blit(block.image, camera.apply(block))

    for block in treasure_blocks:
        screen.blit(block.image, camera.apply(block))
        screen.blit(block.coin, camera.apply(block))

    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))
    
    handle_collisions(player, blocks)
    handle_collisions(player, treasure_blocks)

    pygame.display.flip()  # Update the display
    clock.tick(FPS)

pygame.quit()
sys.exit()
