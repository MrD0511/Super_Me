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
from goombas import Goombas

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
coins = pygame.sprite.Group()
collidable_objs = pygame.sprite.Group()
collidable_enimies = pygame.sprite.Group()
goomabases = pygame.sprite.Group()

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
    "           B   g       b       g g        g                        ",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGGGGGGGGGGGG",
]

camera = Camera(len(level_map[0]) * 32, len(level_map) * 32, SCREEN_WIDTH, SCREEN_HEIGHT)
for row_index,row in enumerate(level_map):
    for col_index, col in enumerate(row):
        if col == 'G':
            block = Ground_Block(col_index*32, row_index*32)
            collidable_objs.add(block)
            ground_blocks.add(block)
        
        elif col == 'g':
            goomabas = Goombas(col_index*32, row_index*32)
            collidable_enimies.add(goomabas)
            goomabases.add(goomabas)

        elif col == 'C':
            cloud = Small_Cloud(col_index*32, row_index*32)
            clouds.add(cloud)

        elif col == 'P':
            tube = Tube(col_index*32, row_index*32)
            collidable_objs.add(tube)
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
            collidable_objs.add(block)
            blocks.add(block)

        elif col == 'T':
            block = Treasure_Block(col_index*32, row_index*32)
            collidable_objs.add(block)
            treasure_blocks.add(block)


player = Player(100, SCREEN_HEIGHT - 4 * 32 )
# Set up display
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(collidable_objs, collidable_enimies)
    camera.update(player)
    blocks.update()
    treasure_blocks.update(coins)
    coins.update()
    goomabases.update(collidable_objs)
    
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

    for coin in coins:
        screen.blit(coin.image, camera.apply(coin))

    for goomabas in goomabases:
        screen.blit(goomabas.image, camera.apply(goomabas))

    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))


    pygame.display.flip()  # Update the display
    clock.tick(FPS)

pygame.quit()
sys.exit()
