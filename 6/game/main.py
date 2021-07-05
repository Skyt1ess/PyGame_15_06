import pygame
from random import randint
from player import Player
from enemy import Enemy

pygame.init()

size=[500, 600]
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
laguna = (7, 235, 250)


shoot_sound = pygame.mixer.Sound("sound/pew.wav")
boom_sound = pygame.mixer.Sound("sound/boom.wav")
shoot_sound.set_volume(0.3)
boom_sound.set_volume(0.3)


pygame.mixer.music.load("sound/melod.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


background = pygame.image.load("img/back.jpg")
bullet_img = pygame.image.load("img/bullet.png").convert()
player_img = pygame.image.load("img/player.png").convert()
player_img = pygame.transform.scale(player_img, (player_img.get_width()//2,
                                    player_img.get_height()//2))
bullet_img = pygame.transform.scale(bullet_img, (bullet_img.get_width(),
                                    bullet_img.get_height()//2))

meteor_img = []
m_list = ['meteor1.png',
          'meteor2.png',
          'meteor3.png',
          'meteor4.png',
          'meteor5.png']

for img in m_list:
    meteor_img.append(pygame.image.load("img/"+ img).convert())




all_sprites = pygame.sprite.Group()
enems = pygame.sprite.Group()
bullets = pygame.sprite.Group()


player = Player(size, player_img)
for i in range(5):
    ind = randint(0, len(meteor_img) - 1)
    enemy = Enemy(size, meteor_img[ind])
    all_sprites.add(enemy)
    enems.add(enemy)


all_sprites.add(player)
game = True


def check_collision():
    for enemy in enems:
        for bullet in bullets:
            if enemy.rect.colliderect(bullet):
                enemy.rect.center
                enemy.kill()
                bullet.kill()
                boom_sound.play(0)
                ind = randint(0, len(meteor_img) - 1)
                newEnem = Enemy(size, meteor_img[ind])
                all_sprites.add(newEnem)
                enems.add(newEnem)
        if enemy.rect.bottom > size[1]:
            enemy.kill()
            ind = randint(0, len(meteor_img) - 1)
            newEnem = Enemy(size, meteor_img[ind])
            all_sprites.add(newEnem)
            enems.add(newEnem)


while game:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets, bullet_img)
                shoot_sound.play(0)

    check_collision()
    display.blit(background, (0, 0))
    all_sprites.update(size)
    all_sprites.draw(display)
    pygame.display.update()

