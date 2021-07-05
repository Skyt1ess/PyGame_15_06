import pygame
import random
import time
pygame.init()

size=[600, 400]
display = pygame.display.set_mode(size)

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
block_size = 10
snake_list =[]
snake_len = 1

x1 = 300
y1 = 300


foodx = round(random.randrange(0, size[0] - block_size) / 10.0) * 10.0
foody = round(random.randrange(0, size[1] - block_size) / 10.0) * 10.0

font_style = pygame.font.SysFont(None, 50)
point_style = pygame.font.SysFont(None, 20)

game_over = False
delta =[0,0]
#fon = pygame.image.load('fon.jpg').convert()

clock = pygame.time.Clock()

def print_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green,
                         [x[0], x[1], block_size, block_size])
    if len(snake_list) > 1:
        k = len(snake_list)
        pygame.draw.rect(display, white,
                         [snake_list[k-1][0], snake_list[k-1][1],
                          block_size, block_size])


def key_down(event):
    if event.key == pygame.K_LEFT:
        delta = [-block_size, 0]
    if event.key == pygame.K_RIGHT:
        delta = [block_size, 0]
    if event.key == pygame.K_DOWN:
        delta = [0, block_size]
    if event.key == pygame.K_UP:
        delta = [0, -block_size]
    return delta

def print_point():
    value = point_style.render("Point: " + str(snake_len - 1), True, white)
    display.blit(value, [5, 5])

def message(text):
    mes = font_style.render(text, True, white)
    display.blit(mes, [size[0]/2, size[1]/2])



while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_over = True
        if event.type == pygame.KEYDOWN:
            delta = key_down(event)

    if x1 >= size[0] or x1 < 0 or y1 >= size[1] or y1 <0:
        game_over = True


    x1 += delta[0]
    y1 += delta[1]
    display.fill((0,0,0))
    #display.blit(fon, (0,0))
    pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])
    pygame.draw.rect(display, white, [x1, y1, block_size, block_size])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)
    if len(snake_list) > snake_len:
        del snake_list[0]

    print_snake(snake_list)
    print_point()
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, size[0] - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, size[1] - block_size) / 10.0) * 10.0
        snake_len += 1



    clock.tick(20)

message("Игра окончена")
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()