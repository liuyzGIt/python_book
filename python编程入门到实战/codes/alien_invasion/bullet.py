import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
        子弹管理类
        继承自Sprite类，可以在游戏中将相关的元素编组，同时操作编组中所有元素
    """
    def __init__(self, ai_settings, screen, ship):
        """在飞船的位置创建一个子弹对象"""
        super().__init__()
        
        self.screen = screen
        
        # 在(0, 0)处创建一个矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
