class Settings:
    
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1
        
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # 外星人设置
        self.alien_speed_facotr = 1
        self.alien_drop_spreed = 10
        # fleet_direction 外星人移动方向，1向右，-1向左
        self.fleet_direction = -1