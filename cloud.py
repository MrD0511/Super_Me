import pygame

tiles = pygame.image.load("./images/platform/tiles.png")

def get_tile( x, y, width, height):
    tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

    tile_surface.blit(tiles, (0,0) , (x,y,height,width) )

    return tile_surface

class Cloud(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('./images/gr_cl_small.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 1

class Small_Cloud(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32*3,32*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.image.fill((0, 140, 250))
        self.image.blit(get_tile(32*10, 0, 32, 32), (0, 0))
        self.image.blit(get_tile(32*8, 0, 32, 32), (32, 0))
        self.image.blit(get_tile(32*12, 0, 32, 32), (64, 0))
        self.image.blit(get_tile(32*9, 0, 32, 32), (0, 32))
        self.image.blit(get_tile(32*7, 0 ,32, 32), (32, 32))
        self.image.blit(get_tile(32*11, 0, 32, 32), (64, 32))