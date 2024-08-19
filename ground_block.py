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
ground_block_tile = get_tile(tiles_image, tile_x, tile_y, 32, 32)

class Ground_Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = ground_block_tile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = get_tile(tiles_image, 32*2, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Treasure_Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = get_tile(tiles_image, 32*3, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, player):

        if self.rect.colliderect(player.rect):
            if player.rect.top <= self.rect.bottom and player.rect.bottom > self.rect.bottom:
                print("Player collided with the bottom of the block!")
                self.rect.y -= 10
                self.rect.y += 10
                

    