import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    外星人管理类
    """
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
        return False


    def update(self):
        self.x += (self.ai_settings.alien_speed_facotr * self.ai_settings.fleet_direction)
        self.rect.x = self.x