#не забудьте переключить раскладку на английскую
import pygame

class Rules:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render('text', 1, (255, 100, 100))
    def update(self):
        # self.title_text = self.font.render('text', 1, (255, 100, 100))
        pass