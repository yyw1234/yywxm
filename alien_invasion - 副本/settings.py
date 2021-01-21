class Settings():
    # 存储《外星人入侵》的所有设置的类
    def __init__(self):
        # 初始化游戏的静态设置
        # 屏幕设置
        # 屏幕的宽度1200，高度800，背景颜色（230, 230, 230）
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置（飞船速度系数：每次移动几个像素）

        self.ship_limit = 3
        # 子弹设置

        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 8

        # 外星人设置
        self.fleet_drop_speed = 15
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随游戏进行而变化的设置
        self.ship_speed_factor = 20
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 3
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 3
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        # 提高速度设置和外星人点数
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
