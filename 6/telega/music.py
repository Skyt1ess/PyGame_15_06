import pygame

pygame.mixer.pre_init(frequency=44100)
#ogg wav
pygame.init()



pygame.mixer.music.load("sounds/bird.mp3")
# mp3 ogg wav
vol = 0.5
musicPause = False

pygame.mixer.music.set_volume(vol)
pygame.mixer.music.play(-1, 0, 0)
size = [900, 570]
display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 60




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                musicPause = not musicPause
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
            if event.key == pygame.K_n:
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_UP:
                vol += 0.1
                vol = min(1.0, vol)
                pygame.mixer.music.set_volume(vol)
                print(pygame.mixer.music.get_volume())
            if event.key == pygame.K_DOWN:
                vol -= 0.1
                vol = max(0.0, vol)
                pygame.mixer.music.set_volume(vol)
                print(pygame.mixer.music.get_volume())


    if musicPause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

    pygame.display.update()
    clock.tick(FPS)