import pygame

from game_object.game_functions import load_image


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

    def update(self):
        pass
        # self.rect = self.rect.move(self.vx, self.vy)
        # if pygame.sprite.spritecollideany(self, self.game.lebron):
        #     self.rect.x = 400
        #     self.rect.y = 400
