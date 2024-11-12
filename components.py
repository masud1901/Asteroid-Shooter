import pygame
from settings import WINDOW_HEIGHT, IMAGES_DIR, load_image
import random


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = load_image("player.png")
        self.rect = self.image.get_rect(center=(640, 360))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = load_image("laser.png")
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, pos, speed):
        super().__init__(groups)
        self.image = load_image("meteor.png")
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = speed
        self.direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1).normalize()

    def update(self):
        self.pos += self.direction * self.speed
        self.rect.topleft = self.pos
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.frames = []
        for i in range(1, 21):
            frame_path = IMAGES_DIR / "explosion" / f"{i}.png"
            if frame_path.exists():
                frame = pygame.image.load(frame_path).convert_alpha()
                self.frames.append(frame)

        self.frame_index = 0
        self.animation_speed = 0.5
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, groups, pos, type="shield"):
        super().__init__(groups)
        self.type = type
        self.image = load_image(f"powerup_{type}.png")
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 2
        self.direction = pygame.math.Vector2(0, 1)

    def update(self):
        self.pos += self.direction * self.speed
        self.rect.topleft = self.pos
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
