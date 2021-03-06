import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类"""
    
    def __init__(self, screen, ai_settings):
        """初始化飞船并设置初始位置"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图片并获取器外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # 新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
