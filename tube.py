import pygame

class Tube(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('./images/tube.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    