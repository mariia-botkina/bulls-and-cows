import pygame
import sys
import random
from grass import Grass
from buttons import Button, Sign

def events(cow): #обработка событий
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_a:
                            cow.mvleft = True
                        case pygame.K_d:
                            cow.mvright = True
                        case pygame.K_w:
                            cow.mvup = True
                        case pygame.K_s:
                            cow.mvdown = True
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_a: #отключение движения персонажей
                            cow.mvleft = False
                        case pygame.K_d: #отключение движения персонажей
                            cow.mvright = False
                        case pygame.K_w: #отключение движения персонажей
                            cow.mvup = False
                        case pygame.K_s: #отключение движения персонажей
                            cow.mvdown = False
                        case pygame.K_SPACE: #смена персонажей
                            cow.mv = not cow.mv


def update(bg_color, screen, grasses, cow, boxes, buttons, signs): #обновление экрана
        screen.fill(bg_color)
        for grass in grasses:
            grass.output()
        for button in buttons:
            button.output()  
        for sign in signs:
            sign.output()  
        boxes.output()
        cow.output()
        pygame.display.flip()
        #pygame.display.update()

def create_grass(screen, grasses): #генерация травы на фоне     
    number_of_grass = random.randint(40,80)

    for _ in range(number_of_grass):
        grass = Grass(screen)
        grasses.add(grass)    

def create_buttons(screen, buttons, signs): #генерация кнопок и надписей
    name = [*range(0, 10), 'del', 'enter']
    random.shuffle(name)
    for i in range(12):
        button = Button(screen, i)
        sign = Sign(screen, button, name[i])
        buttons.add(button)  
        signs.add(sign)