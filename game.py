import pygame

from sprites.lebron import Lebron
from game_object.settings import Settings
from game_object.event import EventGame
from sprites.ball import Ball

class Game:
    def __init__(self):
        # cоздадим настройки
        self.ai_settings = Settings()

        # инициализация окна
        pygame.init()
        self.size = self.width, self.height = self.ai_settings.screen_width, self.ai_settings.screen_height
        self.screen = pygame.display.set_mode()   
        self.screen.blit(self.ai_settings.background_image, (0, 0))
        pygame.display.set_caption('Basketball')
        pygame.display.flip()

        # настройка цыкла
        self.clock = pygame.time.Clock()
        
        self.running = True

    def new(self):
        self.playing = True
        # создадим группу, содержащую все спрайты
        self.all_sprites = pygame.sprite.Group()

        # создадим lebron
        self.lebron = Lebron(self, self.ai_settings)
        self.all_sprites.add(self.lebron)

        # создадим ball
        self.ball = Ball(self, self.ai_settings)
        self.all_sprites.add(self.ball)

        # инициализация класса событий
        self.event_game = EventGame(self, self.lebron)

    def events(self):
        self.event_game.check_events()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.ai_settings.background_image, (0, 0))
        self.all_sprites.draw(self.screen)

        self.clock.tick(self.ai_settings.fps)

        pygame.display.flip()


    def main(self):
        # основной цыкл игры
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
        pygame.quit()

    def game_over(self):
        pass

    def intro_screen(self):
        pass
