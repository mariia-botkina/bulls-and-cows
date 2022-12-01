import pygame
import pygame.sprite

class Button(pygame.spite.Spites): #класс кнопок с цифрами на поле
    def __init__(self, screen):
        super(Button, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/button.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.top = self.screen_rect.top/4
        self.rect.right = self.screen_rect.right/2

    def output(self):
        self.screen.blit(self.image, self.rect)


