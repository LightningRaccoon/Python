import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
t=0
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            t += 1
            print(t)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                running = False
    pygame.display.update()