import pygame

class Big_Mountain(pygame.sprite.Sprite):

    def __init__(self, x ,y):
        super().__init__()
        self.tiles = pygame.image.load("./images/platform/tiles.png")
        self.image = pygame.Surface((32*5,32*3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.image.fill((0, 140, 250))
        self.image.blit(self.get_tile(32, 32, 32, 32), (32, 64))
        self.image.blit(self.get_tile(0, 32, 32, 32), (64, 64))
        self.image.blit(self.get_tile(32*2, 32, 32, 32), (0, 64))
        self.image.blit(self.get_tile(32*2, 32, 32, 32), (32, 32))
        self.image.blit(self.get_tile(32, 32, 32, 32), (64, 32)) 
        self.image.blit(self.get_tile(32*4, 32, 32, 32), (128, 64))
        self.image.blit(self.get_tile(32, 32, 32, 32), (96, 64)) 
        self.image.blit(self.get_tile(32*4, 32, 32, 32), (96, 32))
        self.image.blit(self.get_tile(32*3, 32, 32, 32), (64, 0))

    def get_tile(self, x, y, width, height):

        tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

        tile_surface.blit(self.tiles, (0,0) , (x,y,height,width) )

        return tile_surface