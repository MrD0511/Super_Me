import pygame

class Camera():

    def __init__(self, width, height, screen_width, screen_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.camera_viewport = pygame.Rect(0, 0, width, height)
        self.SCREEN_HEIGHT = screen_height
        self.SCREEN_WIDTH = screen_width

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self,target):

        x = -target.rect.centerx + int(self.SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(self.SCREEN_HEIGHT / 2)

        x = min(0,x)
        y = min(0,y)

        x = max( -(self.camera.width - self.SCREEN_WIDTH), x)
        y = max( -(self.camera.height - self.SCREEN_HEIGHT), y)

        self.camera = pygame.Rect(x, y , self.camera.width, self.camera.height)