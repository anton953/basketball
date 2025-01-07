import pygame
import os
import sys

from game_object.game_functions import load_image


class Lebron(pygame.sprite.Sprite):

    def __init__(self, game, ai_settings, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)

        self.image = load_image("lebron_23_3.png").convert_alpha()
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
     
   
    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.moving_right and self.rect.right < self.game.screen.get_width():
            self.x_change += self.speed
            self.facing = 'right'
        if self.moving_left and self.rect.left > 0:
            self.x_change -= self.speed
            self.facing = 'left'
    
        if self.moving_back and self.rect.bottom < self.game.screen.get_height():
            self.y_change += self.speed
            self.facing = 'back'
        if self.moving_forward and self.rect.top > 0:
            self.y_change -= self.speed
            self.facing = 'forward'
