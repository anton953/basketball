import pygame

import os
import sys

from lebron import Lebron
from settings import Settings
# from game_functions import load_image
from event import EventGame
from ball import Ball

class Game:
    def __init__(self):
        
        # cоздадим настройки
        self.ai_settings = Settings()

        # инициализация окна
        pygame.init()
        self.size = self.width, self.height = self.ai_settings.screen_width, self.ai_settings.screen_height
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.ai_settings.bg_color)
        pygame.display.set_caption('Basketball')
        pygame.display.flip()


        # создадим группу, содержащую все спрайты
        self.all_sprites = pygame.sprite.Group()


        # создадим спрайт
        self.lebron = Lebron(self.screen, self.ai_settings)

        # добавим спрайт в группу
        self.all_sprites.add(self.lebron)

        self.ball = Ball(self.screen, self.ai_settings)
        self.all_sprites.add(self.ball)

        # инициализация класса событий
        self.event_game = EventGame(self.lebron)

        # настройка цыкла
        self.clock = pygame.time.Clock()

    def start(self):

        # основной цыкл игры
        while True:
            self.screen.blit(self.ai_settings.background_image, (0, 0))

            self.event_game.check_events()
            self.all_sprites.update()

            self.all_sprites.draw(self.screen)

            self.clock.tick(self.ai_settings.fps)

            pygame.display.flip()

        # ожидание закрытия окна:
        # while pygame.event.wait().type != pygame.QUIT:
        #     pass
        # завершение работы:
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.start()