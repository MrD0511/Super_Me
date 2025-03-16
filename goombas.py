import pygame
import os

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)


class Goombas(pygame.sprite.Sprite):

    def __init__(self, x, y):
        """
        Initialize the Goomba enemy.
        
        :param x: Initial x-coordinate position.
        :param y: Initial y-coordinate position.
        """
        super().__init__()

        # Load Goomba animations (two frames for walking animation)
        self.images = [
            pygame.image.load(resource_path('assets/images/goombas_0.png')),
            pygame.image.load(resource_path('assets/images/goombas_1.png'))
        ]
        self.image = self.images[0]  # Start with the first animation frame
        self.rect = self.image.get_rect()
        self.rect.x = x  # Set initial x position
        self.rect.y = y  # Set initial y position

        # Movement direction
        self.direction = 'left'

        # Load dead Goomba image
        self.dead_img = pygame.image.load(resource_path('assets/images/goombas_dead.png'))
        self.is_dead = False  # Flag to track if Goomba is dead
        self.death_time = 0  # Store time of death to handle removal delay

        # Gravity simulation
        self.velocity_y = 0  

        # Animation properties
        self.animation_speed = 200  # Change frame every 200ms
        self.last_update_time = pygame.time.get_ticks()  # Store last animation update time
        self.run_index = 0  # Track animation frame index

        # Activation flag (Goomba starts moving only when the player is nearby)
        self.is_active = False  

        # Movement speed
        self.speed = 2  

    def update(self, collidable_objs, player):
        """
        Update Goomba's movement, animations, and handle collisions.
        
        :param collidable_objs: List of objects (e.g., ground, pipes) that Goomba can collide with.
        :param player: The player object (used to activate movement when nearby).
        """
        # If the Goomba is dead, check if it should be removed
        if self.is_dead:
            if pygame.time.get_ticks() - self.death_time > 500:  # Remove after 500ms
                self.kill()  # Remove from the sprite group
            return  # Skip further updates

        # Activate Goomba when the player is within 500 pixels
        if self.rect.x - player.rect.x < 500:
            self.is_active = True

        # If not activated, do nothing
        if not self.is_active:
            return
    
        # Handle animation timing
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed:
            # Cycle between the two walking frames
            self.run_index = (self.run_index + 1) % len(self.images)
            self.image = self.images[self.run_index]
            self.last_update_time = current_time  # Reset animation timer

        # Store previous position for collision handling
        old_x = self.rect.x  
        old_y = self.rect.y  

        # Move left or right based on direction
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        # Check for horizontal collisions (walls, obstacles)
        for obj in collidable_objs:
            if not self.is_dead and self.rect.colliderect(obj):
                self.rect.x = old_x  # Undo movement
                # Change direction upon hitting an obstacle
                self.direction = 'right' if self.direction == 'left' else 'left'
                break  # Stop checking further collisions

        # Apply gravity (simulated fall)
        self.velocity_y += 1  # Increase downward speed
        if self.velocity_y > 10:  # Cap maximum fall speed
            self.velocity_y = 10

        self.rect.y += self.velocity_y  # Apply vertical movement

        # Check for ground collision
        self.on_ground = False
        for obj in collidable_objs:
            if not self.is_dead and self.rect.colliderect(obj):
                if old_y < obj.rect.top:  # Check if Goomba was above the object before falling
                    self.rect.bottom = obj.rect.top  # Align to the top of the object
                    self.velocity_y = 0  # Reset vertical velocity (stop falling)
                    self.on_ground = True  # Mark as on the ground
                break  # Stop checking further collisions

    def die(self):
        """
        Handles Goomba's death by changing its sprite and scheduling its removal.
        """
        self.image = self.dead_img  # Change sprite to dead Goomba
        self.is_dead = True  # Mark Goomba as dead
        self.death_time = pygame.time.get_ticks()  # Store time of death
