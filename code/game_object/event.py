import pygame


# класс событий
class EventGame:
    def __init__(self, game):
        self.game = game

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.playing = False
                self.game.running = False

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

    def check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.game.lebron.moving_forward = True
        if event.key == pygame.K_s:
            self.game.lebron.moving_back = True
        if event.key == pygame.K_d:
            self.game.lebron.moving_right = True
        if event.key == pygame.K_a:
            self.game.lebron.moving_left = True

        if event.key == pygame.K_e and self.game.ball.moving == False and self.game.lebron.ball_status:
            self.game.all_sprites.add(self.game.ball)

            self.game.ball.rect.x = self.game.lebron.rect.x
            self.game.ball.rect.y = self.game.lebron.rect.y


            self.game.lebron.ball_status = False
            self.game.ball.moving = True
            self.game.ball.ownership = 'a'

            self.game.ball.calculation_cor()


        if event.key == pygame.K_i:
            self.game.zak.moving_forward = True
        if event.key == pygame.K_k:
            self.game.zak.moving_back = True
        if event.key == pygame.K_l:
            self.game.zak.moving_right = True
        if event.key == pygame.K_j:
            self.game.zak.moving_left = True

        if event.key == pygame.K_o and self.game.ball.moving == False and self.game.zak.ball_status:
            self.game.all_sprites.add(self.game.ball)

            self.game.ball.rect.x = self.game.zak.rect.x
            self.game.ball.rect.y = self.game.zak.rect.y


            self.game.zak.ball_status = False
            self.game.ball.moving = True
            self.game.ball.ownership = 'b'

            self.game.ball.calculation_cor()

    def check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.game.lebron.moving_forward = False
        if event.key == pygame.K_s:
            self.game.lebron.moving_back = False
        if event.key == pygame.K_d:
            self.game.lebron.moving_right = False
        if event.key == pygame.K_a:
            self.game.lebron.moving_left = False

        if event.key == pygame.K_i:
            self.game.zak.moving_forward = False
        if event.key == pygame.K_k:
            self.game.zak.moving_back = False
        if event.key == pygame.K_l:
            self.game.zak.moving_right = False
        if event.key == pygame.K_j:
            self.game.zak.moving_left = False


