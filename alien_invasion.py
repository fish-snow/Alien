import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # 创建屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_setting)
    # 创建一个外星人实例
    alien = Alien(ai_setting,screen)
    # 创建一艘飞船
    ship = Ship(ai_setting,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    # 游戏主循环
    while True:
        # 硬件监控
        gf.check_events(ai_setting,screen,ship,bullets)
        ship.update()
        # 删除子弹函数
        gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
        gf.update_aliens(ai_setting, ship, aliens)
        # 绘制屏幕
        gf.update_screen(ai_setting,screen,ship,aliens,bullets)

run_game()
