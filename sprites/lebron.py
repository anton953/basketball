import pygame
import os
import sys

from game_object.game_functions import load_image


class Lebron(pygame.sprite.Sprite):

    def __init__(self, game, ai_settings, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)

        self.image = load_image("img/lebron/lebron_r_1.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.ai_settings = ai_settings
        self.game = game

        self.rect.x = 350
        self.rect.y = 350
        
        self.moving_forward = False
        self.moving_back = False
        self.moving_right = False
        self.moving_left = False
        
        self.speed = ai_settings.speed

        self.ball_status = False

        self.facing = 'down'

        self.x_change = 0
        self.y_change = 0

        self.fps_cnt = 0
     
   
    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

        self.animate()

    def movement(self):
        if self.moving_right and self.rect.right < self.game.screen.get_width():
            self.x_change += self.speed
            self.facing = 'right'
        if self.moving_left and self.rect.left > 0:
            self.x_change -= self.speed
            self.facing = 'left'
    
        if self.moving_back and self.rect.bottom < self.game.screen.get_height():
            self.y_change += self.speed
            self.facing = 'down'
        if self.moving_forward and self.rect.top > 0:
            self.y_change -= self.speed
            self.facing = 'forward'

    def animate(self):
        down_animations = [load_image("img/lebron/lebron_animaton/lebron_f_1.png").convert_alpha(),
                           load_image("img/lebron/lebron_animaton/lebron_f_2.png").convert_alpha()]
        
        up_animations = [load_image("img/lebron/lebron_animaton/lebron_b_1.png").convert_alpha(),
                         load_image("img/lebron/lebron_animaton/lebron_b_2.png").convert_alpha()]
        
        right_animations = [load_image("img/lebron/lebron_animaton/lebron_r_1.png").convert_alpha(),
                            load_image("img/lebron/lebron_animaton/lebron_r_2.png").convert_alpha()]
        
        left_animations = [load_image("img/lebron/lebron_animaton/lebron_l_1.png").convert_alpha(),
                           load_image("img/lebron/lebron_animaton/lebron_l_2.png").convert_alpha()]

        if self.fps_cnt == 60:
                self.fps_cnt = 0

        if self.facing == 'down':
            if self.moving_back:
                self.image = down_animations[0]
            elif self.fps_cnt == 0:
                self.image = down_animations[0]
            elif self.fps_cnt == 50:
                self.image = down_animations[1]

        elif self.facing == 'forward':
            if self.moving_forward:
                self.image = up_animations[0]
            elif self.fps_cnt == 0:
                self.image = up_animations[0]
            elif self.fps_cnt == 50:
                self.image = up_animations[1]

        elif self.facing == 'right':
            if self.moving_right:
                self.image = right_animations[0]
            elif self.fps_cnt == 0:
                self.image = right_animations[0]
            elif self.fps_cnt == 50:
                self.image = right_animations[1]

        elif self.facing == 'left':
            if self.moving_left:
                self.image = left_animations[0]
            elif self.fps_cnt == 0:
                self.image = left_animations[0]
            elif self.fps_cnt == 50:
                self.image = left_animations[1]

        self.fps_cnt += 1
