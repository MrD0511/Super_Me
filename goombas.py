import pygame
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)


class Goombas(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load(resource_path('assets/images/goombas_0.png')),
            pygame.image.load(resource_path('assets/images/goombas_1.png'))
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'left'
        self.dead_img = pygame.image.load(resource_path('assets/images/goombas_dead.png'))
        self.is_dead = False
        self.death_time = 0
        self.velocity_y = 0
        # Animation properties
        self.animation_speed = 200  # Change frame every 200ms
        self.last_update_time = pygame.time.get_ticks()
        self.run_index = 0
        self.is_active = False
        # Movement speed
        self.speed = 2

    def update(self, collidable_objs, player):

        if self.is_dead:
            if pygame.time.get_ticks() -self.death_time > 500:
                self.kill() 
            return
        
        if self.rect.x - player.rect.x < 400:
            self.is_active = True


        if not self.is_active:
            return
    
        # Handle animation timing
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed:
            self.run_index = (self.run_index + 1) % len(self.images)
            self.image = self.images[self.run_index]
            self.last_update_time = current_time  # Reset timer

        old_x = self.rect.x  # Store previous position
        old_y = self.rect.y
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        # Collision detection (check left/right only)
        for obj in collidable_objs:
            if self.rect.colliderect(obj):
                self.rect.x = old_x  # Undo movement
                self.direction = 'right' if self.direction == 'left' else 'left'
                break  # Stop checking further collisions

        # Apply gravity
        self.velocity_y += 1  # Simulate gravity
        if self.velocity_y > 10:  # Limit fall speed
            self.velocity_y = 10

        self.rect.y += self.velocity_y  # Apply vertical movement

        # Check for ground collision
        self.on_ground = False
        for obj in collidable_objs:
            if self.rect.colliderect(obj):
                if old_y < obj.rect.top:  # If it was above the object before falling
                    self.rect.bottom = obj.rect.top  # Place it on top
                    self.velocity_y = 0  # Reset gravity
                    self.on_ground = True
                break  # Stop checking further collisions
    

    def die(self):
        self.image = self.dead_img
        self.is_dead = True
        self.death_time = pygame.time.get_ticks()

