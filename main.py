import pygame
import sys
import random
from pathlib import Path

from components import Ship, Laser, Meteor, Explosion


# Initialize Pygame
pygame.init()
print(f"Pygame version: {pygame.__version__}")
print(f"Pygame initialization status: {pygame.get_init()}")

# Initialize audio
pygame.mixer.init()
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
meteor_group = pygame.sprite.Group()

# timer for meteor spawning
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)  # Spawn meteor every 500ms

# sprite creation
ship = Ship(spaceship_group)

# Load sound effects
laser_sound = pygame.mixer.Sound("space shooter/audio/laser.wav")
explosion_sound = pygame.mixer.Sound("space shooter/audio/explosion.wav")
background_music = pygame.mixer.Sound("space shooter/audio/game_music.wav")
background_music.play(loops=-1)  # Start playing background music on loop


# Add these after the existing initialization code
class GameState:
    WELCOME = "welcome"
    PLAYING = "playing"
    GAME_OVER = "game_over"


# Font setup
font_path = "space shooter/images/Oxanium-Bold.ttf"  # Adjust path if needed
if Path(font_path).exists():
    game_font = pygame.font.Font(font_path, 40)
else:
    game_font = pygame.font.Font(None, 40)  # Fallback to default font

# Game state
current_state = GameState.WELCOME
score = 0

# Additional sprite group for explosions
explosion_group = pygame.sprite.Group()


def draw_text(text, pos):
    text_surface = game_font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=pos)
    display_surface.blit(text_surface, text_rect)


# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == GameState.WELCOME:
                current_state = GameState.PLAYING
            elif current_state == GameState.PLAYING:
                Laser(laser_group, ship.rect.midtop)
                laser_sound.play()  # Play laser sound
            elif current_state == GameState.GAME_OVER:
                # Reset game
                current_state = GameState.PLAYING
                score = 0
                # Clear all sprites
                meteor_group.empty()
                laser_group.empty()
                explosion_group.empty()

        if event.type == meteor_timer and current_state == GameState.PLAYING:
            x_pos = random.randint(0, WINDOW_WIDTH)
            # Add a random speed for each meteor (adjust values as needed)
            meteor_speed = random.uniform(4, 8)
            Meteor(meteor_group, (x_pos, -50), meteor_speed)

    # background
    display_surface.blit(background_image, (0, 0))

    if current_state == GameState.WELCOME:
        draw_text("ASTEROID SHOOTER", (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        draw_text("Click to Start", (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

    elif current_state == GameState.PLAYING:
        # Check for collisions between lasers and meteors
        for laser in laser_group:
            meteors_hit = pygame.sprite.spritecollide(laser, meteor_group, True)
            if meteors_hit:
                laser.kill()
                score += len(meteors_hit)
                for meteor in meteors_hit:
                    Explosion(explosion_group, meteor.rect.center)
                    explosion_sound.play()  # Play explosion sound

        # Check for collisions between ship and meteors
        if pygame.sprite.spritecollide(ship, meteor_group, True):
            current_state = GameState.GAME_OVER
            Explosion(explosion_group, ship.rect.center)
            explosion_sound.play()  # Play explosion sound

        # Update and draw all sprite groups
        spaceship_group.draw(display_surface)
        spaceship_group.update()
        laser_group.draw(display_surface)
        laser_group.update()
        meteor_group.draw(display_surface)
        meteor_group.update()
        explosion_group.draw(display_surface)
        explosion_group.update()

        # Draw score
        draw_text(f"Score: {score}", (WINDOW_WIDTH - 100, 50))

    elif current_state == GameState.GAME_OVER:
        # Continue showing explosions until they're done
        explosion_group.draw(display_surface)
        explosion_group.update()

        draw_text("GAME OVER", (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        draw_text(f"Final Score: {score}", (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        draw_text("Click to Play Again", (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

    # Update the display
    pygame.display.update()

    # Control frame rate
    clock.tick(60)
