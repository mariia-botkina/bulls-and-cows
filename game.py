import pygame, controls
from cow import Cow
from bull import Bull
from boxes import Boxes
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Быки и коровы')
    bg_color = (59, 94, 62)
    cow = Cow(screen)
    bull = Bull(screen)
    boxes = Boxes(screen)
    grasses = Group() 
    buttons = Group()
    signs = Group()
    controls.create_grass(screen, grasses)
    controls.create_buttons(screen, buttons, signs)
    
    while True:
        controls.events(cow, bull)
        cow.update_cow()
        bull.update_bull()
        controls.update(bg_color, screen, grasses, cow, bull, boxes, buttons, signs)

run()