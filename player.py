import pygame
from ground_block import Block, Treasure_Block
from goombas import Goombas
from flag import Pillar
import os
import sys

# Function to get the absolute path of a resource file (ensures compatibility across different environments)
def resource_path(relative_path):
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)

# Load player images for different states
player_idle = pygame.image.load(resource_path('assets/images/Mario/mario.png'))
player_run1 = pygame.image.load(resource_path('assets/images/Mario/mario_move0.png'))
player_run2 = pygame.image.load(resource_path('assets/images/Mario/mario_move1.png')) 
player_run3 = pygame.image.load(resource_path('assets/images/Mario/mario_move2.png'))
player_jump = pygame.image.load(resource_path('assets/images/Mario/mario_jump.png'))
player_end = pygame.image.load(resource_path('assets/images/Mario/mario_end.png'))
player_death = pygame.image.load(resource_path('assets/images/Mario/mario_death.png'))

# Player class representing Mario
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # Set initial player state
        self.image = player_idle.convert_alpha()  # Default image
        self.end_image = player_end  # Image when reaching the flag
        self.rect = self.image.get_rect()  # Get player dimensions
        self.rect.x = x  # Initial X position
        self.rect.y = y  # Initial Y position
        
        # Running animation frames
        self.run_images = [player_run1, player_run3, player_run2]
        
        # Physics and movement variables
        self.velocity_y = 0  # Vertical speed
        self.on_ground = False  # Check if player is on the ground
        self.run_timer = 0  # Animation timer for running
        self.run_index = 0  # Index to track running frames
        self.run_animation_speed = 0.2  # Speed of run animation
        self.direction = 'right'  # Default direction
        self.is_jumping = False  # Jump state
        
        # Game state flags
        self.mario_end = False  # Check if Mario reached the flag
        self.mario_walking_to_castle = False  # Mario walking to castle after flag
        self.game_over = False  # Game over state
        
        # Load sound effects
        self.jumping_sound = pygame.mixer.Sound(resource_path("assets/music/jump.wav"))
        self.jumping_sound.set_volume(0.3)
        self.death_sound = pygame.mixer.Sound(resource_path("assets/music/death.wav"))
        self.death_sound.set_volume(0.3)
        self.levelend_sound = pygame.mixer.Sound(resource_path("assets/music/levelend.wav"))
        self.levelend_sound.set_volume(0.3)

        # Player status variables
        self.mario_dead = False
        self.score = 0
        self.coins = 0

        # Track player movement for scoring
        self.initial = x
        self.current = x

    # Update function to handle movement, collisions, and animations
    def update(self, collidable_objs, collidable_enimies):

        self.current = self.rect.x  # Update current position

        # Increase score when moving forward
        if self.current - self.initial > 30:
            self.score += 10
            self.initial = self.current

        # If game is over, stop updating
        if self.game_over:
            return

        # If Mario reached the flag
        if self.mario_end:
            if self.mario_sliding_down:
                self.rect.y += 5  # Slide down the flagpole
                if self.rect.y >= 320:  # Stop at the bottom of the pole
                    self.mario_sliding_down = False
                    self.mario_walking_to_castle = True  # Start walking to castle

            elif self.mario_walking_to_castle:
                self.run_timer += self.run_animation_speed
                if self.run_timer > 1:
                    self.run_timer = 0
                    self.run_index = (self.run_index + 1) % len(self.run_images)
                self.image = self.run_images[self.run_index]  # Walking animation
                self.rect.x += 3  # Move towards castle
                if self.rect.x >= 7225:  # Stop when reaching castle
                    self.kill()
                    self.game_over = True
                    return
            return  # Stop normal movement
        
        keys = pygame.key.get_pressed()  # Get key inputs

        # Handle running animation when moving
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.run_timer += self.run_animation_speed
            if self.run_timer > 1:
                self.run_timer = 0
                self.run_index = (self.run_index + 1) % len(self.run_images)
            self.image = self.run_images[self.run_index]

            # Move left
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                self.direction = 'left'
                
            # Move right
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
                self.direction = 'right'
        else:
            self.image = player_idle  # If not moving, idle image

        # Flip sprite if moving left
        if self.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

        # Collision handling with objects
        for obj in collidable_objs:
            if not self.mario_dead and self.rect.colliderect(obj.rect):
                if keys[pygame.K_LEFT]:  # Prevent passing through left
                    self.rect.left = obj.rect.right
                if keys[pygame.K_RIGHT]:  # Prevent passing through right
                    self.rect.right = obj.rect.left
                
                # If Mario touches the flagpole
                if isinstance(obj, Pillar):
                    self.mario_end = True
                    self.image = self.end_image  # Mario grabbing flag
                    self.mario_end_animation(obj)

        # Collision handling with enemies
        for obj in collidable_enimies:
            if self.rect.colliderect(obj.rect) and not obj.is_dead:
                if self.velocity_y > 0:  # If falling onto an enemy
                    if isinstance(obj, Goombas):
                        obj.die()  # Kill the enemy
                        self.velocity_y -= 10  # Bounce up slightly
                        self.score += 100  # Increase score
                else:  # If enemy touches Mario from the side
                    self.velocity_y -= 5  # Small jump before death
                    self.death_sound.play()
                    self.image = player_death
                    self.mario_dead = True

        # Jumping logic
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.velocity_y -= 15  # Jump force
            self.on_ground = False
            self.jumping_sound.play()

        # Apply gravity
        self.velocity_y = min(self.velocity_y + 0.83, 10)  # Max fall speed is 10
        self.rect.y += self.velocity_y

        # If Mario is dead, stop updating
        if self.mario_dead:
            self.image = player_death
            return
        
        # If jumping, use jump image
        if not self.on_ground:
            self.image = player_jump
            if self.direction == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
        
        # Reset ground state and handle vertical collisions
        self.on_ground = False
        for obj in collidable_objs:
            if self.rect.colliderect(obj.rect):
                if self.velocity_y > 0:  # Landing on an object
                    self.velocity_y = 0
                    self.rect.bottom = obj.rect.top
                    self.on_ground = True
                elif self.velocity_y < 0 and self.rect.bottom > obj.rect.bottom:  # Hitting a block from below
                    self.rect.top = obj.rect.bottom
                    self.velocity_y = 0
                    if isinstance(obj, Block):
                        obj.is_bouncing = True
                    elif isinstance(obj, Treasure_Block):
                        obj.is_bouncing = True
                        obj.is_hit = True           
                        self.coins += 1  # Collect a coin

    # Animation for Mario reaching the flag
    def mario_end_animation(self, pillar):
        self.image = pygame.transform.flip(self.image, True, False)
        pillar.flag.flag_moving = True  # Move the flag down
        self.rect.x = pillar.rect.x + 5  # Align Mario with flagpole
        self.mario_sliding_down = True  # Start sliding animation
        self.mario_walking_to_castle = False
        self.levelend_sound.play()
