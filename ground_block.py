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
        self.is_bouncing = False
        self.original_y = y
        self.bouncing_timer = 0

    def update(self):
        if self.is_bouncing:
            if self.bouncing_timer < 5:
                self.rect.y -= 2
            elif self.bouncing_timer < 10:
                self.rect.y += 2
            else:
                self.rect.y = self.original_y
                self.is_bouncing = False
                self.bouncing_timer = 0

            self.bouncing_timer += 1
        



class Treasure_Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.images = [get_tile(tiles_image, 32*3, 0, 32, 32), get_tile(tiles_image, 32*4, 0, 32, 32), get_tile(tiles_image, 32*5, 0, 32, 32)]
        self.image = get_tile(tiles_image, 32*3, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_idx = 0
        self.is_bouncing = False
        self.original_y = y
        self.bouncing_timer = 0
        self.current_time = pygame.time.get_ticks()
        self.hited_image = get_tile(tiles_image, 32*6, 0, 32, 32)
        self.animation_speed = 200
        self.last_update_tick = pygame.time.get_ticks()

        self.is_hit = False
        self.coin = None
        self.is_active = True

    def update(self, coins):
        self.current_time = pygame.time.get_ticks()
        
        if self.current_time - self.last_update_tick > 200 and self.is_active:
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.image = self.images[self.image_idx]
            self.last_update_tick = self.current_time

        if self.is_bouncing:
            if self.bouncing_timer < 5:
                self.rect.y -= 2
            elif self.bouncing_timer < 10:
                self.rect.y += 2
            else:
                self.rect.y = self.original_y
                self.is_bouncing = False
                self.bouncing_timer = 0

            self.bouncing_timer += 1
        
        if self.is_hit and self.is_active:
            self.image = self.hited_image
            self.coin = Coin(self.rect.x, self.rect.y - 30)
            coins.add(self.coin)
            self.is_hit = False
            self.is_active = False

class Coin(pygame.sprite.Sprite):
        
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load("./images/coin_an0.png"),
            pygame.image.load("./images/coin_an1.png"),
            pygame.image.load("./images/coin_an2.png"),
            pygame.image.load("./images/coin_an3.png")
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x+16, y))
        self.velocity_y = -3
        self.timer = 5
        self.animation_speed = 200
        self.last_updated_tick = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.image_idx = 0

    def update(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_updated_tick > 200:
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.image = self.images[self.image_idx]
            self.last_updated_tick = self.current_time

        if self.timer < 10:
            self.rect.y -= 5
        elif self.timer < 20:
            self.rect.y += 5
        else:
            self.kill()
        
        self.timer += 1
      