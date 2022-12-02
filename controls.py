import pygame
import sys
import random
from grass import Grass
from buttons import Button, Sign

def events(cow, bull): #обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if cow.mv:
                        cow.mvleft = True
                    else:
                        bull.mvleft = True
                    pass #тут должно быть переключение между боксами с номерами
                elif event.key == pygame.K_d:
                    if cow.mv:
                        cow.mvright = True #тут должно быть переключение между боксами с номерами
                    else:
                        bull.mvright = True
                elif event.key == pygame.K_w:
                    if cow.mv:
                        cow.mvup = True
                    else:
                        bull.mvup = True
                elif event.key == pygame.K_s:
                    if cow.mv:
                        cow.mvdown = True
                    else:
                        bull.mvdown = True
                elif event.key == pygame.K_SPACE:                   
                    pass
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a: #отключение движения персонажей
                    cow.mvleft = False
                    bull.mvleft = False
                elif event.key == pygame.K_d: #отключение движения персонажей
                    cow.mvright = False
                    bull.mvright = False
                elif event.key == pygame.K_w: #отключение движения персонажей
                    cow.mvup = False
                    bull.mvup = False
                elif event.key == pygame.K_s: #отключение движения персонажей
                    cow.mvdown = False
                    bull.mvdown = False
                elif event.key == pygame.K_SPACE: #смена персонажей
                    cow.mv = not cow.mv
                    bull.mv = not bull.mv

def update(bg_color, screen, grasses, cow, bull, boxes, buttons, signs): #обновление экрана
        screen.fill(bg_color)
        for grass in grasses:
            grass.output()
        for button in buttons:
            button.output()  
        for sign in signs:
            sign.output()  
        boxes.output()
        cow.output()
        bull.output()
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