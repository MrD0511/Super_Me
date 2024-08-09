import pygame
import sys
from player import Player
from cloud import Cloud


pygame.init()

SCREEN_HEIGHT = 416
SCREEN_WIDTH = 640


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Bros. Remake")


all_sprites = pygame.sprite.Group()
# Initialize Pygame
clouds = pygame.sprite.Group()

clock = pygame.time.Clock()
# Main game loop
running = True

tiles_image = pygame.image.load("./images/platform/tiles.png")

print(tiles_image)

def get_tile(image, x, y, width, height):

    tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

    tile_surface.blit(image, (0,0) , (x,y,height,width) )

    return tile_surface

TILE_WIDTH = 32
TILE_HEIGHT = 32
tile_x = 0 * TILE_WIDTH  # Third column
tile_y = 0 * TILE_HEIGHT

block_tile = get_tile(tiles_image, tile_x, tile_y, 32, 32)
print(block_tile)


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = block_tile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

blocks = pygame.sprite.Group()


level_map = [
    "                                ",
    "      C                     C   ",
    "                                ",
    "             C                  ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
]


for row_index,row in enumerate(level_map):
    for col_index, col in enumerate(row):
        if col == 'G':
            block = Block(col_index*32, row_index*32)
            blocks.add(block)
        if col == 'C':
            print(col_index, row_index)
            cloud = Cloud(col_index*32, row_index*32)
            clouds.add(cloud)

player = Player(100, SCREEN_HEIGHT - 3 * 32 , blocks= blocks )
# Set up display
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    # Draw everything
    screen.fill((20, 197, 250))  # Clear the screen with a black color
    blocks.draw(screen)
    clouds.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()  # Update the display
    clock.tick(30)
pygame.quit()
sys.exit()
