class Settings:
    
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # self.ship_speed_factor = 1
        self.ship_limit = 3
        
        # 子弹设置
        # self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        # self.alien_speed_facotr = 1
        self.alien_drop_spreed = 10
        # fleet_direction 外星人移动方向，1向右，-1向左
        # self.fleet_direction = -1
        
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_facotr = 1
        self.fleet_direction = -1
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_facotr *= self.speedup_scale
        
