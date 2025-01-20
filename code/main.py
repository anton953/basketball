import pygame
import sys

from game import Game

# Egor branch
 
def main():
    # создание обекта игры
    game = Game()

    # вводный экран
    game.intro_screen()

    # создание спрайтов
    game.new()

    # основной цыкл
    while game.running:
        game.main()
        game.game_over()
    
    # закрытие окон
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()