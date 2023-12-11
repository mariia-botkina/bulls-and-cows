import pygame, controls

import rules
from cow import Cow
from boxes import Boxes
from pygame.sprite import Group
from rules import Rules

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Bulls and cows')
    bg_color = (59, 94, 62)
    cow = Cow(screen)
    boxes = Boxes(screen)
    grasses = Group() 
    buttons = Group()
    signs = Group()
    rules = Rules()
    controls.create_grass(screen, grasses)
    controls.create_buttons(screen, buttons, signs)
    
    while True:
        controls.events(cow)
        cow.update_cow()
        controls.update(bg_color, screen, grasses, cow, boxes, buttons, signs, rules)

run()