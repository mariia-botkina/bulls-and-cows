import pygame
import random

class Bull():
    def __init__(self, screen): #инициализация быка
        self.screen = screen

        image = random.choice([self.left_bull, self.right_bull]) #случайный выбор между положениями коровы
        image() #выполнение выбранной функции
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx/2
        self.x = float(self.screen_rect.centerx/2)
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.screen_rect.centery)

        self.rect.bottom = self.screen_rect.bottom/3 * 2

        self.mv = False
        self.mvright = False
        self.mvleft = False
        self.mvup = False
        self.mvdown = False

    def output(self): #отрисовка быка
        self.screen.blit(self.image, self.rect)

    def update_bull(self): #обновление позиции быка
        if self.mvright and self.rect.right < self.screen_rect.right:
            self.right_bull()
            self.x += 0.75
        if self.mvleft and self.rect.left > self.screen_rect.left:
            self.left_bull()
            self.x -= 0.75
        if self.mvup and self.rect.top > self.screen_rect.top:
            self.y -= 0.75
        if self.mvdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += 0.75
        
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def left_bull(self): #задание левосторонней быка
        self.image = pygame.image.load('images/bull_left.png')

    def right_bull(self): #задание правосторонней быка
        self.image = pygame.image.load('images/bull_right.png')
