import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, size, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(size[0] - self.rect.width)
        self.rect.y = random.randrange(0, 20)
        self.speedx = random.randrange(-2, 3)
        self.speedy = random.randrange(1, 5)

    def update(self, size):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.randrange(1, 3)
        if self.rect.right > size[0]:
            self.rect.right = size[0]
            self.speedx = random.randrange(-2, 0)
