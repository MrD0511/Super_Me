import pygame
from ground_block import Block, Treasure_Block
from goombas import Goombas

player_idle = pygame.image.load('./images/mario/mario.png')
player_run1 = pygame.image.load('./images/mario/mario_move0.png')
player_run2 = pygame.image.load('./images/mario/mario_move1.png') 
player_run3 = pygame.image.load('./images/mario/mario_move2.png')
player_jump = pygame.image.load('./images/mario/mario_jump.png')

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = player_idle.convert_alpha()
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

    def update(self, collidable_objs, collidable_enimies):
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
            if self.rect.colliderect(obj.rect):
                if keys[pygame.K_LEFT]:  # If moving left
                    self.rect.left = obj.rect.right
                if keys[pygame.K_RIGHT]:  # If moving right
                    self.rect.right = obj.rect.left

        for obj in collidable_enimies:
            if self.rect.colliderect(obj.rect):
                if keys[pygame.K_LEFT]:  # If moving left
                    self.rect.left = obj.rect.right
                if keys[pygame.K_RIGHT]:  # If moving right
                    self.rect.right = obj.rect.left
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground :
            self.velocity_y -= 15
            self.on_ground = False

        self.velocity_y = min(self.velocity_y + 1, 10)  # Max fall speed is 10
        self.rect.y += self.velocity_y

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

        for obj in collidable_enimies:
            if self.rect.colliderect(obj.rect):
                if self.velocity_y > 0:
                    if isinstance(obj, Goombas):
                        obj.die()


        




                

                    
                
                
                


        