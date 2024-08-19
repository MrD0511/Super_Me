import pygame

player_idle = pygame.image.load('./images/mario/mario.png')
player_run1 = pygame.image.load('./images/mario/mario_move0.png')
player_run2 = pygame.image.load('./images/mario/mario_move1.png') 
player_run3 = pygame.image.load('./images/mario/mario_move2.png')
player_jump = pygame.image.load('./images/mario/mario_jump.png')

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, ground, tubes):
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
        self.ground = ground
        self.tubes = tubes

    def update(self):
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

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.velocity_y -= 15
            self.on_ground = False

        self.velocity_y += 1
        self.rect.y += self.velocity_y

        if not self.on_ground:
            self.image = player_jump

            if self.direction == 'left':
                self.image = pygame.transform.flip(self.image, True, False)


        for block in self.ground:
            if self.rect.colliderect(block.rect):
                if self.velocity_y > 0:
                    self.rect.bottom =  block.rect.top
                    self.velocity_y = 0
                    self.on_ground = True

        for tube in self.tubes:
            if self.rect.colliderect(tube.rect):
                if self.velocity_y > 0:
                    self.rect.bottom =  tube.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.direction == 'right':
                    self.rect.right = tube.rect.left
                else:
                    self.rect.left = tube.rect.right

        