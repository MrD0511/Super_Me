import pygame

class Pillar(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        
        self.image = pygame.image.load('./images/flag_pillar.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.flag = Flag(x + 10, self.image.get_height() - 235)

    def update(self):
        if self.flag.flag_moving and self.flag.rect.y < self.rect.y + 240:
            self.flag.rect.y += 5  # Move flag down slowly

class Flag(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        
        self.image = pygame.transform.flip(pygame.image.load('./images/flag.png'), True, False)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.flag_moving = False

