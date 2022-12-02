import pygame
import pygame.sprite
import random

class Button(pygame.sprite.Sprite): #класс кнопок с цифрами на поле
    def __init__(self, screen, i):
        place = [[3.5, 1], [2, 1.219], [1.1281, 1.0828], [1, 4], [1.2, 2], [1.6, 1.5], [1.5, 1.001], [2, 2], [2.1, 4.72891], [1.103, 1.4], [1.4, 2.919], [3.6, 5.7]]

        super(Button, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/button.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom / place[i][0] - 20
        self.rect.right = self.screen_rect.right / place[i][1] - 20

    def output(self):
        self.screen.blit(self.image, self.rect)

class Sign(pygame.sprite.Sprite): #класс надписей на кнопках
    
    def __init__(self, screen, button, name):

        super(Sign, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(f'images/{name}.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottomleft = button.rect.bottomleft
        
    
    def output(self):
        self.screen.blit(self.image, self.rect)

