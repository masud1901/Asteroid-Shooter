import pygame
from pathlib import Path

# Display settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

# Asset paths
GAME_DIR = Path("space shooter")
IMAGES_DIR = GAME_DIR / "images"
AUDIO_DIR = GAME_DIR / "audio"
FONT_PATH = IMAGES_DIR / "Oxanium-Bold.ttf"

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game settings
INITIAL_LIVES = 3
METEOR_SPAWN_TIME = 1500  # milliseconds
METEOR_SPAWN_REDUCTION = 100  # Reduce spawn time by this amount
MIN_METEOR_SPAWN_TIME = 250  # Minimum spawn time
DIFFICULTY_INCREASE_SCORE = 10  # Increase difficulty every X points

# Speed settings
LASER_SPEED = 10
INITIAL_METEOR_SPEED = 3
METEOR_SPEED_INCREMENT = 0.5
MAX_METEOR_SPEED = 8

# Power-up settings
POWERUP_SPAWN_CHANCE = 0.05  # 5% chance per meteor
SHIELD_DURATION = 5000  # milliseconds

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()


# Load assets
def load_image(name):
    return pygame.image.load(IMAGES_DIR / name).convert_alpha()


def load_sound(name):
    return pygame.mixer.Sound(AUDIO_DIR / name)


# Load font
if FONT_PATH.exists():
    GAME_FONT = pygame.font.Font(FONT_PATH, 40)
else:
    GAME_FONT = pygame.font.Font(None, 40)
