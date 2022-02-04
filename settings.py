class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (219, 255, 223)

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6  # limit bullets

        # aliens settings
        self.fleet_drop_speed = 10  # speed to drop the fleet down

        self.ship_limit = 3  # count of ships in game (like as life?)

        # game speed boost (aliens boost)
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        # init the changes into game speed
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.fleet_direction = 1  # neg to left, pos to right

        # get points
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
