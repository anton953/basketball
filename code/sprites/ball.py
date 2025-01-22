import pygame

from game_object.game_functions import load_image, movement

import math

# класс мяча
class Ball(pygame.sprite.Sprite):
    image = load_image("img/ball/ball_2.png")

    def __init__(self, game, ai_settings, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Ball.image
        self.rect = self.image.get_rect()

        self.ai_settings = ai_settings
        self.game = game

        self.rect.x = 15
        self.rect.y = 15

        self.cx = 20
        self.cy = 20

        self.mouving = True

        self.move_size = 0

        self.speed = self.ai_settings.speed_ball

        self.x_bufer = 0
        self.y_bufer = 0

        self.px = 0
        self.py = 0

    def update(self):
        self.move()

    def mov(self):
        s = (abs(self.rect.x - self.cx) ** 2 + abs(self.rect.y - self.cy) ** 2) ** 0.5

        self.px = abs(self.rect.x - self.cx) / (s / 2)
        self.py = abs(self.rect.y - self.cy) / (s / 2)
    
    def move(self):
        if self.cx > self.rect.x:
            if self.x_bufer > 1:
                self.rect.x += 1 * self.speed
        elif self.cx < self.rect.x:
            if self.x_bufer > 1:
                self.rect.x -= 1 * self.speed

        if self.cy > self.rect.y:
            if self.y_bufer > 1:
                self.rect.y += self.move_size * self.speed 
        elif self.cy < self.rect.y:
            if self.y_bufer > 1:
                self.rect.y -= self.move_size * self.speed
        
        self.x_bufer += self.px
        self.y_bufer += self.py




    # def move(self, cen, s):  # функция передвижения
    #     x = self.rect.center[0]
    #     y = self.rect.center[1]
    #     g = ((x - cen[0]) * 2 + (y - cen[1]) * 2) * 0.5
    #     if g == 0:
    #         return
    #     u = math.asin((y - cen[1]) / g)
    #     res = [int(round(abs(s * math.cos(u)))), int(round(abs(s * math.cos(math.pi / 2 - u))))]
    #     if x < cen[0]:
    #         res[0] = x + res[0]
    #     else:
    #         res[0] = x - res[0]
    #     if y < cen[1]:
    #         res[1] = y + res[1]
    #     else:
    #         res[1] = y - res[1]
    #     self.rect.center = res
