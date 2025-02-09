import pygame

from sprites.lebron import Lebron
from sprites.zak import Zak
from game_object.settings import Settings
from game_object.event import EventGame
from sprites.ball import Ball
from game_object.button import Button
from game_object.game_functions import colo


class Game:
    def __init__(self):
        # cоздадим настройки
        self.ai_settings = Settings()

        # инициализация окна
        pygame.init()
        self.size = self.width, self.height = self.ai_settings.screen_width, self.ai_settings.screen_height
        self.screen = pygame.display.set_mode(self.size)   
        pygame.display.set_caption('Basketball')
        pygame.display.flip()

        # настройка цыкла
        self.clock = pygame.time.Clock()
        
        self.running = True

        self.font = pygame.font.Font('code/data/font/Roboto-Bold.ttf', 32)

        self.count_a = 0
        self.count_b = 0


    # создание спрайтов
    def new(self):
        self.playing = True
        # создадим группу, содержащую все спрайты
        self.all_sprites = pygame.sprite.Group()

        # создадим lebron
        self.lebron = Lebron(self, self.ai_settings)
        self.all_sprites.add(self.lebron)

        self.zak = Zak(self, self.ai_settings)
        self.all_sprites.add(self.zak)

        print(self.lebron.rect)

        # создадим ball
        self.ball = Ball(self, self.ai_settings)

        # инициализация класса событий
        self.event_game = EventGame(self)

    # события игры
    def events(self):
        self.event_game.check_events()

    # обновление экрана
    def update(self):
        self.all_sprites.update()

    # отрисовка экрана
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.ai_settings.background_image, (0, 0))

        score = self.font.render(f'{self.count_a}:{self.count_b} {self.ball.status}', True, colo(self.ball.status))
        score_rect = score.get_rect(x=374, y=575)
        self.screen.blit(score, score_rect)
    
        
        self.all_sprites.draw(self.screen)

        self.clock.tick(self.ai_settings.fps)

        pygame.display.flip()

    # основной цыкл игры
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
        pygame.quit()

    # окончание игры
    def game_over(self):
        pass

    #  вводный экран
    def intro_screen(self):
        print(self.screen.get_width)
        intro = True

        title = self.font.render('Basketball', True, (0, 0, 0))
        title_rect = title.get_rect(x=self.width // 2 - 60, y=self.height // 2 - 50)

        play_button = Button(self.width // 2 - 60, self.height // 2, 100, 50, ('white'), (0, 0, 0), 'play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.fill(pygame.Color((103, 58, 183)), (0, 0, self.width // 2, self.height))
            self.screen.fill(pygame.Color((222, 3, 3)), (self.width // 2, self.height, self.width // 2, self.height))

            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)

            self.clock.tick(self.ai_settings.fps)
            pygame.display.update()

    def upp_score(self, player):
        if player == 'L':
            self.count_a += 1
        elif player == 'Z':
            self.count_b += 1

        if self.count_a == self.ai_settings.max_score or self.count_b == self.ai_settings.max_score:
            print('ff')
            self.playing = False

