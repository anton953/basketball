import pygame

import os
import sys

from lebron import Lebron
from settings import Settings
# from game_functions import load_image
from event import EventGame

def main():
    # cоздадим настройки
    ai_settings = Settings()

    # инициализация окна
    pygame.init()
    size = width, height = ai_settings.screen_width, ai_settings.screen_height
    screen = pygame.display.set_mode(size)
    screen.fill(ai_settings.bg_color)
    pygame.display.set_caption('Basketball')
    pygame.display.flip()

    screen.get_width


   # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()


    # создадим спрайт
    sprite = Lebron(screen, ai_settings)

    # добавим спрайт в группу
    all_sprites.add(sprite)

    # инициализация класса событий
    event_game = EventGame(sprite)

    # настройка цыкла
    running = True
    clock = pygame.time.Clock()

    # основной цыкл игры
    while running:
        screen.blit(ai_settings.background_image, (0, 0))

        sprite.update()
        event_game.check_events()

        all_sprites.draw(screen)

        clock.tick(ai_settings.fps)

        pygame.display.flip()

    # ожидание закрытия окна:
    # while pygame.event.wait().type != pygame.QUIT:
    #     pass
    # завершение работы:
    pygame.quit()


if __name__ == '__main__':
    main()