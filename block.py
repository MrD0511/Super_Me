import pygame

def get_tile(image, x, y, width, height):

    tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

    tile_surface.blit(image, (0,0) , (x,y,height,width) )

    return tile_surface


tiles_image = pygame.image.load("./images/platform/tiles.png")
TILE_WIDTH = 32
TILE_HEIGHT = 32
tile_x = 0 * TILE_WIDTH  # Third column
tile_y = 0 * TILE_HEIGHT
block_tile = get_tile(tiles_image, tile_x, tile_y, 32, 32)


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = block_tile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y