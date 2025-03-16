import pygame
import os

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)

def get_tile(image, x, y, width, height):
    """Extracts a tile from a larger tileset image."""
    tile_surface = pygame.Surface((height, width), pygame.SRCALPHA)  # Create a transparent surface
    tile_surface.blit(image, (0, 0), (x, y, height, width))  # Blit the tile onto the surface
    return tile_surface

# Load the tileset image
tiles_image = pygame.image.load(resource_path("assets/images/platform/tiles.png"))

# Define tile dimensions
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Get a specific tile for the ground block
tile_x = 0 * TILE_WIDTH  
tile_y = 0 * TILE_HEIGHT
ground_block_tile = get_tile(tiles_image, tile_x, tile_y, 32, 32)

# Ground Block class
class Ground_Block(pygame.sprite.Sprite):
    """Represents a static ground block in the game."""

    def __init__(self, x, y):
        super().__init__()
        self.image = ground_block_tile  # Assign the tile image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Block class (breakable/question block)
class Block(pygame.sprite.Sprite):
    """Represents a block that bounces when hit from below."""

    def __init__(self, x, y):
        super().__init__()
        self.image = get_tile(tiles_image, 32 * 2, 0, 32, 32)  # Get block tile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_bouncing = False  # Track if the block is bouncing
        self.original_y = y  # Store original y position
        self.bouncing_timer = 0
        self.block_hit_sound = pygame.mixer.Sound(resource_path("assets/music/blockhit.wav"))  # Load sound effect

    def update(self):
        """Handles block bouncing animation when hit from below."""
        if self.is_bouncing:
            if self.bouncing_timer < 5:  # Move up for the first 5 frames
                self.rect.y -= 2
            elif self.bouncing_timer < 10:  # Move down for the next 5 frames
                self.rect.y += 2
            else:  # Reset position and stop bouncing
                self.rect.y = self.original_y
                self.is_bouncing = False
                self.bouncing_timer = 0

            self.bouncing_timer += 1  # Increment the timer

# Treasure Block class (question block containing a coin)
class Treasure_Block(pygame.sprite.Sprite):
    """Represents a treasure block that releases a coin when hit."""

    def __init__(self, x, y):
        super().__init__()
        # Load animation frames for the question block
        self.images = [
            get_tile(tiles_image, 32 * 3, 0, 32, 32),  
            get_tile(tiles_image, 32 * 4, 0, 32, 32),  
            get_tile(tiles_image, 32 * 5, 0, 32, 32)
        ]
        self.image = self.images[0]  # Start with the first frame
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_idx = 0
        self.is_bouncing = False
        self.original_y = y
        self.bouncing_timer = 0
        self.current_time = pygame.time.get_ticks()
        self.hited_image = get_tile(tiles_image, 32 * 6, 0, 32, 32)  # Image when block is hit
        self.animation_speed = 200  # Animation speed in milliseconds
        self.last_update_tick = pygame.time.get_ticks()
        self.coin_sound = pygame.mixer.Sound(resource_path("assets/music/coin.wav"))  # Load coin sound
        self.coin_sound.set_volume(0.3)
        self.is_hit = False
        self.coin = None
        self.is_active = True  # Active state to prevent multiple coin spawns

    def update(self, coins):
        """Updates block animation and handles coin spawning when hit."""
        self.current_time = pygame.time.get_ticks()

        # Animate block if it's still active
        if self.current_time - self.last_update_tick > 200 and self.is_active:
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.image = self.images[self.image_idx]
            self.last_update_tick = self.current_time

        # Handle block bounce animation
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
        
        # Handle block hit and spawn coin
        if self.is_hit and self.is_active:
            self.is_active = False  # Mark block as inactive
            self.image = self.hited_image  # Change image to used block
            self.coin = Coin(self.rect.x, self.rect.y - 30)  # Create a coin
            coins.add(self.coin)  # Add coin to coin group
            self.is_hit = False
            self.coin_sound.play()  # Play coin sound

# Coin class
class Coin(pygame.sprite.Sprite):
    """Represents a collectible coin that appears after hitting a Treasure Block."""

    def __init__(self, x, y):
        super().__init__()
        # Load coin animation frames
        self.images = [
            pygame.image.load(resource_path("assets/images/coin_an0.png")),
            pygame.image.load(resource_path("assets/images/coin_an1.png")),
            pygame.image.load(resource_path("assets/images/coin_an2.png")),
            pygame.image.load(resource_path("assets/images/coin_an3.png"))
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x + 16, y))
        self.velocity_y = -3  # Upward movement speed
        self.timer = 5  # Controls how long the coin moves
        self.animation_speed = 200  # Animation speed in milliseconds
        self.last_updated_tick = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.image_idx = 0

    def update(self):
        """Updates coin animation and handles movement."""
        self.current_time = pygame.time.get_ticks()

        # Animate coin by cycling through images
        if self.current_time - self.last_updated_tick > 200:
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.image = self.images[self.image_idx]
            self.last_updated_tick = self.current_time

        # Move the coin upwards, then downwards, then disappear
        if self.timer < 15:
            self.rect.y -= 5  # Move up
        elif self.timer < 30:
            self.rect.y += 5  # Move down
        else:
            self.kill()  # Remove coin from game after animation ends
        
        self.timer += 1  # Increment timer

# Stone class
class Stone(pygame.sprite.Sprite):
    """Represents an indestructible stone block."""

    def __init__(self, x, y):
        super().__init__()
        self.image = get_tile(tiles_image, 32 * 1, 0, 32, 32)  # Load stone tile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
