import pygame
import random

class Grass(pygame.sprite.Sprite): #класс травы на фоне
    def __init__(self, screen): #инициализируем и создаем траву
        super(Grass, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(f'images/grass{random.randint(1,5)}.png') #случайный выбор вида травы из 5 возможных
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom * random.random() 
        self.rect.right = self.screen_rect.right * random.random()

    def output(self): #вывод травы на экран
        self.screen.blit(self.image, self.rect)