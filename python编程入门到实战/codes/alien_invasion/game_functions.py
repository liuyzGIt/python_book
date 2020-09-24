import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(screen, ai_settings, ship, aliens, bullets):
    """绘制屏幕"""
    screen.fill(ai_settings.bg_color)  
    
    for bullet in bullets:
        bullet.draw_bullet()
      
    # 绘制飞船
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    # 每执行一次循环都会绘制一个屏幕，擦除旧屏幕
    # 不断的更新屏幕，显示元素位置。营造平滑效果
    pygame.display.flip()


def update_bullets(bullets, screen, ai_settings, ship, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(screen, ai_settings, bullets, aliens, ship)


def check_bullet_alien_collisions(screen, ai_settings, bullets, aliens, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(screen, ai_settings, ship, aliens)


def check_fleet_edge(aliens, ai_settings):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(aliens, ai_settings)
            break


def change_fleet_direction(aliens, ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_spreed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens, ship):
    check_fleet_edge(aliens, ai_settings)
    aliens.update()
    for alien in aliens.copy():
        if alien.rect.top > ai_settings.screen_height:
            aliens.remove(alien)
    if pygame.sprite.spritecollideany(ship, aliens):
        print("ship hit!!")


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(screen, ai_settings, ship,  aliens):
    alien = Alien(screen, ai_settings)
    number_aliens = get_alien_number(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    create_alien(ai_settings, screen, aliens, number_aliens, number_rows)


def get_alien_number(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens = available_space_x // (2 * alien_width)
    return number_aliens


def create_alien(ai_settings, screen, aliens, number_aliens, number_rows):
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            alien = Alien(screen, ai_settings)
            alien_width = alien.rect.width
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = available_space_y // (2 * alien_height)
    return number_rows