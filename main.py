import pygame
import sys

from components import Ship, Laser


# Initialize Pygame
pygame.init()
print(f"Pygame version: {pygame.__version__}")
print(f"Pygame initialization status: {pygame.get_init()}")

# Set up the display
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# background
background_image = pygame.image.load("space shooter/images/background.png")

# sprite groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create laser at ship's position
            Laser(laser_group, ship.rect.midtop)

    # background
    display_surface.blit(background_image, (0, 0))

    # graphics
    spaceship_group.draw(display_surface)
    spaceship_group.update()
    laser_group.draw(display_surface)
    laser_group.update()

    # Update the display
    pygame.display.update()

    # Control frame rate
    clock.tick(60)
