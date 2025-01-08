import pygame

class Settings():
    def __init__(self):
        self.screen_width = 750
        self.screen_height = 588

        self.bg_color = (0, 0, 0)
        self.fps = 60

        self.speed = 2
        
        self.background_image = pygame.image.load('data/img/bord/bord2.png')
