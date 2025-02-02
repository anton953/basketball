import pygame

# класс настроек игры
class Settings():
    def __init__(self):
        self.screen_width = 804
        self.screen_height = 658

        self.bg_color = (0, 0, 0)
        self.fps = 60

        self.speed = 2

        self.speed_ball = 4

        self.cx = 382
        self.cy = 86

        self.background_image = pygame.image.load('code/data/img/bord/bord_lay.png')
