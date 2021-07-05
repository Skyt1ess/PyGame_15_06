import pygame
import random
import time
pygame.init()

size=[500, 600]
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
laguna = (7, 235, 250)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(laguna)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.bottom = size[1] - 10
        self.speedx = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -10
        if key[pygame.K_RIGHT]:
            self.speedx = 10

        if self.rect.right > size[0]:
            self.rect.right = size[0]
        if self.rect.left < 0:
            self.rect.left = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(size[0] - self.rect.width)
        self.rect.y = random.randrange(0, 20)
        self.speedx = random.randrange(-2, 3)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.randrange(1, 3)
        if self.rect.right > size[0]:
            self.rect.right = size[0]
            self.speedx = random.randrange(-2, 0)


all_sprites = pygame.sprite.Group()
enems = pygame.sprite.Group()
bullets = pygame.sprite.Group()


player = Player()
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enems.add(enemy)


all_sprites.add(player)
game = True


def check_collision():
    for enemy in enems:
        for bullet in bullets:
            if enemy.rect.colliderect(bullet):
                all_sprites.remove(enemy)
                all_sprites.remove(bullet)
                bullets.remove(bullet)
                enems.remove(enemy)
                enemy.kill()
                bullet.kill()


while game:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    check_collision()
    display.fill(white)
    all_sprites.update()
    all_sprites.draw(display)
    pygame.display.update()

