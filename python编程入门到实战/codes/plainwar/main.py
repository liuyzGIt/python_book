import sys
import time

import pygame
from pygame.sprite import Group

from settings import Settings


def run_game():
    pygame.init()  # 初始化数据，保证正常运行
    ai_settings = Settings()

    '''
    screen是一个surface, surface是屏幕的一部分，每个元素如飞船都是一个surface
    创建一个名为s显示窗口
    '''
    screen=pygame.display.set_mode((480,700))
    pygame.display.set_caption('Alien Invasion')
    background = pygame.image.load('images/background.png') 
    
    # 开始游戏主循环
    while True:
        #screen.blit(background,(0,0))
        screen.fill((230,230,230))
        # pygame.display.update()   
        pygame.display.flip()
        #time.sleep(1) 
       

run_game()
