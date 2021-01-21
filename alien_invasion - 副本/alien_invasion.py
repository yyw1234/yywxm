import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 创建屏幕对象
    screen = pygame.display.set_mode((1200, 800))  # 屏幕的尺寸为1200*800
    pygame.display.set_caption("Alien Invasion")  # 标题
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 背景音乐
    # 音乐的路径
    # 初始化
    pygame.mixer.init()
    pygame.mixer.music.load("images\纯音乐 - 遇见 (钢琴版) [mqms].mp3")
    pygame.mixer.music.play()

    # 开始游戏的主循环
    while True:
        # 事件驱动：监视键盘和鼠标事件
        # 循环检查所获取的所有事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)





run_game()
