import pygame

class Grass():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/grass1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx/3
        self.rect.bottom = self.screen_rect.bottom/3

    def output(self):
        self.screen.blit(self.image, self.rect)