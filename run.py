import pygame

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# keeps the code going
while True:
    # input -event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    # nothing yet

    # render
    pygame.display.update()
