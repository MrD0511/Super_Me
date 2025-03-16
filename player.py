import pygame
from ground_block import Block, Treasure_Block
from goombas import Goombas
from flag import Pillar
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)

player_idle = pygame.image.load(resource_path('assets/images/Mario/mario.png'))
player_run1 = pygame.image.load(resource_path('assets/images/Mario/mario_move0.png'))
player_run2 = pygame.image.load(resource_path('assets/images/Mario/mario_move1.png')) 
player_run3 = pygame.image.load(resource_path('assets/images/Mario/mario_move2.png'))
player_jump = pygame.image.load(resource_path('assets/images/Mario/mario_jump.png'))
player_end = pygame.image.load(resource_path('assets/images/Mario/mario_end.png'))
player_death = pygame.image.load(resource_path('assets/images/Mario/mario_death.png'))

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = player_idle.convert_alpha()
        self.end_image = player_end
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.run_images = [ player_run1, player_run3, player_run2]
        self.velocity_y = 0
        self.on_ground = False
        self.run_timer = 0
        self.run_index = 0
        self.run_animation_speed = 0.2
        self.direction = 'right'
        self.is_jumping = False
        self.mario_end = False
        self.mario_walking_to_castle = False
        self.game_over = False
        self.jumping_sound = pygame.mixer.Sound(resource_path("assets/music/jump.wav"))
        self.jumping_sound.set_volume(0.3)
        self.mario_dead = False
        self.death_sound = pygame.mixer.Sound(resource_path("assets/music/death.wav"))
        self.death_sound.set_volume(0.3)
        self.score = 0
        self.levelend_sound = pygame.mixer.Sound(resource_path("assets/music/levelend.wav"))
        self.levelend_sound.set_volume(0.3)
        self.coins = 0
        self.initial = x
        self.current = x

    def update(self, collidable_objs, collidable_enimies):

        self.current = self.rect.x

        if self.current - self.initial > 30:
            self.score += 10
            self.initial = self.current

        if self.game_over:
            return

        if self.mario_end:
            if self.mario_sliding_down:
                self.rect.y += 5  # Slide down
                if self.rect.y >= 320:  # Stop at the base of the pole
                    self.mario_sliding_down = False
                    self.mario_walking_to_castle = True  # Start walking

            elif self.mario_walking_to_castle:
                self.run_timer += self.run_animation_speed
                if self.run_timer > 1:
                    self.run_timer = 0
                    self.run_index = (self.run_index + 1) % len(self.run_images)
                self.image = self.run_images[self.run_index]  # Walking animation
                self.rect.x += 3  # Walk towards the castle
                if self.rect.x >= 7225:
                    self.kill()
                    self.game_over = True
                    return

            return  # Stop normal movement
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.run_timer += self.run_animation_speed
            if self.run_timer > 1:
                self.run_timer = 0
                self.run_index = (self.run_index + 1) % len(self.run_images)
            self.image = self.run_images[self.run_index]

            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                self.direction = 'left'
                
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
                self.direction = 'right'
        else:
            self.image = player_idle
            
        if self.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

        for obj in collidable_objs:
            if not self.mario_dead and self.rect.colliderect(obj.rect):
                if keys[pygame.K_LEFT]:  # If moving left
                    self.rect.left = obj.rect.right
                if keys[pygame.K_RIGHT]:  # If moving right
                    self.rect.right = obj.rect.left
                if isinstance(obj, Pillar):
                    self.mario_end = True
                    self.image = self.end_image  # Mario grabbing flag
                    self.mario_end_animation(obj)


        for obj in collidable_enimies:
            if self.rect.colliderect(obj.rect) and not obj.is_dead:
                if self.velocity_y > 0:
                    if isinstance(obj, Goombas):
                        obj.die()
                        self.velocity_y -= 10
                        self.score += 100
                elif (self.rect.right > obj.rect.left and self.rect.left < obj.rect.left) or (self.rect.left < obj.rect.right and self.rect.right > obj.rect.right):
                    self.velocity_y -= 5
                    self.death_sound.play()
                    self.image = player_death
                    self.mario_dead = True

        
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground :
            self.velocity_y -= 15
            self.on_ground = False
            self.jumping_sound.play()

        self.velocity_y = min(self.velocity_y + 0.83, 10)  # Max fall speed is 10
        self.rect.y += self.velocity_y

        if self.mario_dead:
            self.image = player_death
            return
        
        if not self.on_ground:
            self.image = player_jump

            if self.direction == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
        
        self.on_ground = False
        for obj in collidable_objs:
            if self.rect.colliderect(obj.rect):
                if self.velocity_y > 0:
                    self.velocity_y = 0
                    self.rect.bottom = obj.rect.top
                    self.on_ground = True
                elif self.velocity_y < 0 and self.rect.bottom > obj.rect.bottom:
                    self.rect.top = obj.rect.bottom
                    self.velocity_y = 0
                    if isinstance(obj, Block):
                        obj.is_bouncing = True
                    elif isinstance(obj, Treasure_Block):
                        obj.is_bouncing = True
                        obj.is_hit = True           
                        self.coins += 1


    def mario_end_animation(self, pillar):
        self.image = pygame.transform.flip(self.image, True, False)
        pillar.flag.flag_moving = True  # Start flag movement
        self.rect.x = pillar.rect.x + 5  # Align Mario with the pillar
        self.mario_sliding_down = True  # Flag to slide Mario down
        self.mario_walking_to_castle = False
        self.levelend_sound.play()