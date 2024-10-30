import pygame
import sys

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(title="Onek Mojar Game")

clock = pygame.time.Clock()

ship_surf = pygame.image.load(
    "../asteroid_shooter_files/project_1 - blank window/graphics/ship.png"
).convert_alpha()

ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

bg_surf = pygame.image.load(
    "../asteroid_shooter_files/project_1 - blank window/graphics/background.png"
).convert()

# adding font
font = pygame.font.Font(
    "../asteroid_shooter_files/project_1 - blank window/graphics/subatomic.ttf", 50
)
text_surf = font.render("Space", True, "White")
text_rect = text_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))

while True:
    # input -event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # frame rate limit
    clock.tick(60)

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()
    # update
    pygame.display.update()

    # update
    display_surface.fill((200, 200, 200))
    display_surface.blit(bg_surf, (0, 0))
    display_surface.blit(text_surf, text_rect)
    display_surface.blit(
        ship_surf,
        ship_rect,
    )

    # render
    pygame.display.update()
