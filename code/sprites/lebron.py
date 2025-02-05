import pygame
import os
import sys

from game_object.game_functions import load_image


# спрайт леброн
class Lebron(pygame.sprite.Sprite):

    def __init__(self, game, ai_settings, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)

        self.image = load_image("lebron/lebron_animaton_static/lebron_b_1.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.ai_settings = ai_settings
        self.game = game

        self.rect.x = 350
        self.rect.y = 445

        self.moving_forward = False
        self.moving_back = False
        self.moving_right = False
        self.moving_left = False

        self.speed = ai_settings.speed


        self.facing = 'b'

        self.x_change = 0
        self.y_change = 0

        self.fps_cnt = 0

        self.ball_cnt = 1

        # включить или выключить анимацию
        self.ball_status = True

        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        if pygame.sprite.collide_mask(self, self.game.ball) and (self.game.ball.moving == False or self.game.ball.status == 'Z') and self.game.zak.ball_status == False:
            self.ball_status = True
            self.game.ball.moving = False
            self.game.ball.remove(self.game.all_sprites)
            self.game.ball.status = 'L'
        self.movement()

        # old_rect = self.rect.copy

        self.rect.x += self.x_change
        self.rect.y += self.y_change
        if pygame.sprite.pygame.sprite.collide_mask(self, self.game.zak) and self.check_move():
            # self.rect = old_rect
            self.rect.x -= self.x_change
            self.rect.y -= self.y_change

            self.game.zak.rect.x += self.x_change
            self.game.zak.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

        self.animate()

    def movement(self):
        if self.moving_right and self.rect.right < self.game.screen.get_width():
            self.x_change += self.speed
            self.facing = 'r'
        if self.moving_left and self.rect.left > 0:
            self.x_change -= self.speed
            self.facing = 'l'

        if self.moving_back and self.rect.bottom < self.game.screen.get_height():
            self.y_change += self.speed
            self.facing = 'f'
        if self.moving_forward and self.rect.top > 0:
            self.y_change -= self.speed
            self.facing = 'b'

    def animate(self):
        if self.fps_cnt == 60:
            self.fps_cnt = 0

        if self.check_move() and self.ball_status:
            self.ball_anim()
            self.image = load_image(f'lebron/lebron_animaton_ball/lebron_ball_{self.facing}_{self.ball_cnt}.png')
        elif self.check_move():
            self.image = load_image(f'lebron/lebron_animaton_static/lebron_{self.facing}_1.png')
        elif self.ball_status:
            self.ball_anim()
            self.image = load_image(f'lebron/lebron_animaton_ball/lebron_ball_{self.facing}_{self.ball_cnt}.png')
        else:
            self.image = load_image(f'lebron/lebron_animaton_static/lebron_{self.facing}_{1 if 50 > self.fps_cnt >= 0 else 2}.png')

        self.fps_cnt += 1

    def check_move(self):
        if self.moving_forward or self.moving_back or self.moving_left or self.moving_right:
            return True
        return False

    def ball_anim(self):
        if self.fps_cnt % 10 == 0:
            self.ball_cnt += 1

        if self.ball_cnt == 5:
            self.ball_cnt = 1

