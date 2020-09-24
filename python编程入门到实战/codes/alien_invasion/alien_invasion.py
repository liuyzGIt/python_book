import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    
    pygame.init() # 初始化数据，保证正常运行
    ai_settings = Settings()
    
    '''
    screen是一个surface, surface是屏幕的一部分，每个元素如飞船都是一个surface
    创建一个名为s显示窗口
    '''
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) 
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建飞船
    ship = Ship(screen, ai_settings)
    # 创建子弹编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(screen, ai_settings, ship, aliens)
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, screen, ai_settings, ship, aliens)
        gf.update_aliens(ai_settings, aliens, ship)
        gf.update_screen(screen, ai_settings, ship, aliens,  bullets)
    

run_game()
