import pygame

class Boxes:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/boxes.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom / 4

    def output(self):
        self.screen.blit(self.image, self.rect)