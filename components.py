import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "space shooter/images/player.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(center=(640, 360))

    def update(self):
        # Follow mouse position
        self.rect.center = pygame.mouse.get_pos()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load("space shooter/images/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        # Move the laser upward
        self.rect.y -= 10
        # Destroy if it goes off screen
        if self.rect.bottom < 0:
            self.kill()
