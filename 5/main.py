import pygame
from random import randint
from ball import Ball
from telega import Telega


pygame.init()



size = [900, 570]

display = pygame.display.set_mode(size)
pygame.time.set_timer(pygame.USEREVENT, 2000)

clock = pygame.time.Clock()
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
ground = 20

score_bg = pygame.image.load('images/score_fon.png').convert_alpha()
score_font = pygame.font.SysFont('arial', 30)
score = 0

bg = pygame.image.load('images/back1.jpg').convert()

balls_data = ({'image': 'images/ball_bear.png', 'score': 100},
              {'image': 'images/ball_fox.png', 'score': 150},
              {'image': 'images/ball_lion.png', 'score': 200})


balls = pygame.sprite.Group()


telega = Telega(size[0] / 2, size[1])

def createBall():
    index = randint(0, len(balls_data) - 1)
    balls.add(Ball(size[0], balls_data[index]['image'], balls_data[index]['score']))


def collideBalls():
    global score
    for ball in balls:
        if telega.rect.collidepoint(ball.rect.center):
            score += ball.score
            ball.kill()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.USEREVENT:
            createBall()


    balls.update(size[1], ground)
    telega.update(size[0])

    collideBalls()

    display.blit(bg, (0, 0))
    balls.draw(display)

    score_text = score_font.render(str(score), True, (95, 140, 15))
    display.blit(score_bg, (0, 0))
    display.blit(score_text, (20, 10))

    display.blit(telega.image, telega.rect)

    pygame.display.update()
    clock.tick(FPS)