import sys

import pygame

from bullet import Bullet


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
        

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """事件处理"""
    # 监视键盘行业鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
            


def update_screen(screen, ai_settings, ship, bullets):
    """绘制屏幕"""
    screen.fill(ai_settings.bg_color)  
    
    for bullet in bullets:
        bullet.draw_bullet()
      
    # 绘制飞船
    ship.blitme()    
    # 让最近绘制的屏幕可见
    # 每执行一次循环都会绘制一个屏幕，擦除旧屏幕
    # 不断的更新屏幕，显示元素位置。营造平滑效果
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
