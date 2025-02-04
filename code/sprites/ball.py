import pygame

from game_object.game_functions import load_image, movement

import math

# класс мяча
class Ball(pygame.sprite.Sprite):
    image = load_image("ball/ball_2.png")

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

        self.cx = self.ai_settings.cx
        self.cy = self.ai_settings.cy

        self.moving = False

        self.move_size = 0

        self.speed = self.ai_settings.speed_ball

        self.x_bufer = 0
        self.y_bufer = 0

        self.px = 0
        self.py = 0

        self.direction_x = True
        self.direction_y = True

        self.moving_x = True
        self.moving_y = True

    def update(self):
        self.move()

    def calculation_cor(self):
        self.x_bufer = 0
        self.y_bufer = 0

        x = abs(self.rect.x - self.cx)
        y = abs(self.rect.y - self.cy)

        s = (x ** 2 + y ** 2) ** 0.5
        if s == 0:
            print('stop')
            self.moving = False
            return None

        self.px = round(x / s * self.speed, 3)
        self.py = round(y / s * self.speed, 3)

        print(self.px, self.py, self.px, self.py)

        if self.cx > self.rect.x:
            self.direction_x, self.moving_x = True, True
        elif self.cx < self.rect.x:
            self.direction_x, self.moving_x = False, False

        if self.cy > self.rect.y:
            self.direction_y, self.moving_y = True, True
        elif self.cy < self.rect.y:
            self.direction_y, self.moving_y = False, False

    def move(self):
        if self.moving:
            if self.cx > self.rect.x:
                if self.x_bufer >= 1:
                    self.rect.x += int(self.x_bufer)
                    self.x_bufer -= int(self.x_bufer)
                    self.moving_x = True
            elif self.cx < self.rect.x:
                if self.x_bufer >= 1:    
                    self.rect.x -= int(self.x_bufer)
                    self.x_bufer -= int(self.x_bufer)
                    self.moving_x = False

            if self.cy > self.rect.y:
                if self.y_bufer >= 1:
                    self.rect.y += int(self.y_bufer)
                    self.y_bufer -= int(self.y_bufer)
                    self.moving_y = True
            elif self.cy < self.rect.y:
                if self.y_bufer >= 1:
                    self.rect.y -= int(self.y_bufer)
                    self.y_bufer -= int(self.y_bufer)
                    self.moving_y = False
            
            if self.rect.x == self.cx and self.rect.y == self.cy:
                self.moving = False

            elif self.direction_x != self.moving_x or self.direction_y != self.moving_y:
                self.rect.x = self.cx
                self.rect.y = self.cy

                self.moving = False
            
            self.x_bufer += self.px
            self.y_bufer += self.py



    def start_move(self, x, y):
        self.rect.x = x
        self.rect.y = y