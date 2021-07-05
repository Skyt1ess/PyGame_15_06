import pygame
pygame.init()

size = [600, 400]

display = pygame.display.set_mode(size)

clock = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color = (128, 128, 128)

ground = size[1] - 50
jump_force = 20
move = jump_force + 1

hero = pygame.Surface((40, 50))
hero.fill(blue)
rect = hero.get_rect(centerx = size[0] / 2, bottom = ground)


display.fill(red)

pygame.draw.rect(display, color, (0, size[1] - 50, size[0], 50))
pygame.display.update()
rect_update2 = pygame.Rect(0, 0, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force
            if event.key == pygame.K_LEFT:
                rect.x -= 5
                rect_update2 = pygame.Rect(rect.x + rect.width, 0, 5, ground)

    #-10, -9, -8 .. 0 .. 1, 2, 3.. 10
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1


    display.fill(red)
    display.blit(hero, rect)
    rect_update = pygame.Rect(rect.x, 0, rect.width, ground)
    pygame.display.update(rect_update2)
    pygame.display.update(rect_update)
    clock.tick(30)

