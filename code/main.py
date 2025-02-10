import pygame
import sys

from game import Game

# main branch this is test

def main():
    # создание обекта игры
    game = Game()

    # вводный экран
    game.intro_screen()

    # создание спрайтов
    game.new()

    # основной цикл
    while game.running:
        game.main()
        game.game_over()
        game.exit_screen()

    
    # закрытие окон
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()