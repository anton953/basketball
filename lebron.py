import pygame

from game_functions import load_image


class Lebron(pygame.sprite.Sprite):
    image = load_image("lebron_23_2.png")

    def __init__(self, screen, ai_settings, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Lebron.image
        self.rect = self.image.get_rect()

        self.ai_settings = ai_settings
        self.screen = screen

        self.rect.x = 350
        self.rect.y = 350
        
        self.moving_forward = False
        self.moving_back = False
        self.moving_right = False
        self.moving_left = False
        
        self.speed = ai_settings.speed

        self.ball_status = False
     
   
    def update(self):
        if self.moving_right and self.rect.right < self.screen.get_width():
            self.right()
        if self.moving_left and self.rect.left > 0:
            self.left()  
    
        if self.moving_back and self.rect.bottom < self.screen.get_height():
            self.back()
        if self.moving_forward and self.rect.top > 0:
            self.forward() 

    def forward(self):
        if self.moving_forward:
            self.rect.y -= self.speed

    def back(self):
        if self.moving_back:
            self.rect.y += self.speed

    def right(self):
        if self.moving_right:
            self.rect.x += self.speed

    def left(self):
        if self.moving_left:
            self.rect.x -= self.speed
