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

    def update(self):
        self.move([self.cx, self.cy], 3)

    def mov(self):
        m = movement(self.rect.x, self.rect.y, 3, self.cx, self.cy)
        if m:
            self.rect.x = m[0]
            self.rect.y = m[1]
        # if self.mouving:
        #     self.rect.x += 1
        #     self.rect.y += 1

    def move(self, cen, s):  # функция передвижения
        x = self.rect.center[0]
        y = self.rect.center[1]
        g = ((x - cen[0]) * 2 + (y - cen[1]) * 2) * 0.5
        if g == 0:
            return
        u = math.asin((y - cen[1]) / g)
        res = [int(round(abs(s * math.cos(u)))), int(round(abs(s * math.cos(math.pi / 2 - u))))]
        if x < cen[0]:
            res[0] = x + res[0]
        else:
            res[0] = x - res[0]
        if y < cen[1]:
            res[1] = y + res[1]
        else:
            res[1] = y - res[1]
        self.rect.center = res
