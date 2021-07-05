import pygame
pygame.init()


size = [600, 400]

display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 30

white = (255, 255, 255)
red = (255, 0, 0)
yellow = (240, 230, 170)

car_surf = pygame.image.load('images/car.bmp').convert()
car_surf = pygame.transform.scale(car_surf,
                                  (car_surf.get_width() // 3,
                                   car_surf.get_height() // 3))
finish_surf = pygame.image.load('images/finish.png')
background = pygame.image.load('images/sand.jpg').convert()

car_surf.set_colorkey(white)
car_rect = car_surf.get_rect(center=(size[0] / 2, size[1] / 2))

background = pygame.transform.scale(background,
                                    (background.get_width() // 3,
                                     background.get_height() // 3))



car_up = car_surf
car_down = pygame.transform.flip(car_surf, False, True)
car_left = pygame.transform.rotate(car_surf, 90)
car_right = pygame.transform.flip(car_left, True, False)
car_rightup = pygame.transform.rotate(car_surf, -45)
car_rightdown = pygame.transform.rotate(car_surf, -135)
car_leftup = pygame.transform.rotate(car_surf, 45)
car_leftdown = pygame.transform.rotate(car_surf, 135)
car = car_up
left = right = down = False
up = True
speed = 5

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key = pygame.key.get_pressed()

    if key[pygame.K_a]:
        left = True
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    else:
        left = False

    if key[pygame.K_d]:
        right = True
        car = car_right
        car_rect.x += speed
        if car_rect.right > size[0]:
            car_rect.right = size[0]
    else:
        right = False

    if key[pygame.K_w]:
        up = True
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    else:
        up = False

    if key[pygame.K_s]:
        down = True
        car = car_down
        car_rect.y += speed
        if car_rect.bottom > size[1]:
            car_rect.bottom = size[1]
    else:
        down = False

    if up and right:
        car = car_rightup
    if up and left:
        car = car_leftup
    if down and right:
        car = car_rightdown
    if down and left:
        car = car_leftdown

    car_rect = car.get_rect(center=(car_rect.center))


    display.blit(background, (0, 0))
    display.blit(finish_surf, (0, 0))
    display.blit(car, car_rect)
    pygame.display.update()

