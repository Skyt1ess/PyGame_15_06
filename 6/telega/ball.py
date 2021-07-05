import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, widht, filename, score):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(random.randrange(0 + self.image.get_width(),
                                     widht - self.image.get_width()), 0))
        self.speed = random.randrange(1, 4)
        self.score = score


    def update(self, *args):
        if self.rect.y < args[0] - args[1]:
            self.rect.y += self.speed
        else:
            self.kill()
