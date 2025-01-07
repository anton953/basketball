import pygame
import sys

from game import Game

def main():
    game = Game()
    game.intro_screen()
    game.new()
    while game.running:
        game.main()
        game.game_over()
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()