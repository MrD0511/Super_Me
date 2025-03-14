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
        self.y = y
        self.is_up = False

        self.coin = pygame.image.load("./images/coin_an0.png")
        self.coin_rect = self.coin.get_rect()
        self.coin_rect.x = x+8
        self.coin_rect.y = y+8
        
    def update(self, player):

        if self.is_up:
            self.rect.y += 1

        if self.rect.y == self.y:
            self.is_up = False

        if self.rect.colliderect(player.rect):
            if player.rect.top <= self.rect.bottom and not self.is_up:
                print("Player collided with the bottom of the block!")
                self.rect.y -= 10
                self.is_up = True
                player.velocity_y += 15
                player.rect.y += player.velocity_y

def handle_collisions(player, blocks):
    collisions = pygame.sprite.spritecollide(player, blocks, False)
    
    for block in collisions:
        # Determine the direction of the collision
        if player.rect.bottom < block.rect.top and player.rect.centery < block.rect.centery:
            player.rect.bottom = block.rect.top
        elif player.rect.top <= block.rect.bottom and player.rect.centery > block.rect.centery:
            player.rect.top = block.rect.bottom
        elif player.rect.right >= block.rect.left and player.rect.centerx < block.rect.centerx:
            player.rect.right = block.rect.left
        elif player.rect.left <= block.rect.right and player.rect.centerx > block.rect.centerx:
            player.rect.left = block.rect.right

        # Ensure the player’s velocity is zeroed or handled appropriately after collision
        # (e.g., setting velocity to 0 in case you have a movement mechanism)

      