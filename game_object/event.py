import pygame

# класс событий
class EventGame:
    def __init__(self, game, sprite1):
        self.sprite1 = sprite1
        self.game = game

    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.playing = False
                    self.game.running = False

                elif event.type == pygame.KEYDOWN:
                   self.check_keydown_events(event, self.sprite1)
                   
                elif event.type == pygame.KEYUP:
                   self.check_keyup_events(event, self.sprite1)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.ball.mouving = True
                    self.game.ball.cx = event.pos[0]
                    self.game.ball.cy = event.pos[1]

    def check_keydown_events(self, event, sprite):
        if event.key == pygame.K_w:
            sprite.moving_forward = True
        if event.key == pygame.K_s:
            sprite.moving_back = True
        if event.key == pygame.K_d:
            sprite.moving_right = True
        if event.key == pygame.K_a:
            sprite.moving_left = True

    def check_keyup_events(self, event, sprite):
        if event.key == pygame.K_w:
            sprite.moving_forward = False
        if event.key == pygame.K_s:
            sprite.moving_back = False
        if event.key == pygame.K_d:
            sprite.moving_right = False
        if event.key == pygame.K_a:
            sprite.moving_left = False

