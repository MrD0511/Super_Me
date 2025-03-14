import pygame

class Goombas(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load('./images/goombas_0.png'),
            pygame.image.load('./images/goombas_1.png')
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'left'
        self.dead_img = pygame.image.load('./images/goombas_dead.png')
        self.is_dead = False
        self.death_time = 0
        # Animation properties
        self.animation_speed = 200  # Change frame every 200ms
        self.last_update_time = pygame.time.get_ticks()
        self.run_index = 0

        # Movement speed
        self.speed = 3

    def update(self, collidable_objs):

        if self.is_dead:
            if pygame.time.get_ticks() -self.death_time > 500:
                self.kill() 
            return

        old_x = self.rect.x  # Store previous position
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
        
        # Handle animation timing
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed:
            self.run_index = (self.run_index + 1) % len(self.images)
            self.image = self.images[self.run_index]
            self.last_update_time = current_time  # Reset timer

        # Move Goomba

        # Collision detection (check left/right only)
        for obj in collidable_objs:
            if self.rect.colliderect(obj):
                self.rect.x = old_x  # Undo movement
                self.direction = 'right' if self.direction == 'left' else 'left'
                break  # Stop checking further collisions

    
    def die(self):
        self.image = self.dead_img
        self.is_dead = True
        self.death_time = pygame.time.get_ticks()

