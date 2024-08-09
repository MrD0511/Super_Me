import pygame

class Cloud(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('./images/gr_cl_small.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

