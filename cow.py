import pygame
import random

class Cow():

    def __init__(self, screen): #инициализация коровы
        self.screen = screen

        image = random.choice([self.left_cow, self.right_cow]) #случайный выбор между положениями коровы
        image() #выполнение выбранной функции
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx / 5 * random.randint(2, 7)
        self.x = float(self.rect.centerx)
        self.rect.centery = self.screen_rect.centery / 5 * random.randint(2, 7)
        self.y = float(self.rect.centery)

        self.mv = True
        self.mvright = False
        self.mvleft = False
        self.mvup = False
        self.mvdown = False

    def output(self): #отрисовка коровы
        self.screen.blit(self.image, self.rect)

    def update_cow(self): #обновление позиции коровы
        step = 1.25
        if self.mvright and self.rect.right < self.screen_rect.right:
            self.right_cow()
            self.x += step 
        if self.mvleft and self.rect.left > self.screen_rect.left:
            self.left_cow()
            self.x -= step 
        if self.mvup and self.rect.top > self.screen_rect.top:
            self.y -= step 
        if self.mvdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += step 
        
        self.rect.centerx = self.x
        self.rect.centery = self.y
    
    def left_cow(self): #задание левосторонней коровы
        self.image = pygame.image.load('images/cow_left.png')

    def right_cow(self): #задание правосторонней коровы
        self.image = pygame.image.load('images/cow_right.png')

           