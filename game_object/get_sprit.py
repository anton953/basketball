import pygame

class GetSprite:
    def __init__(self, file):
        self.image = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.image,  (0, 0), (x, y, width, height))
        