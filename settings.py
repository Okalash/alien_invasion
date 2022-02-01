
class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (219, 255, 223)
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6  # limit bullets

        # aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10  # speed to drop the fleet down
        self.fleet_direction = 1  # neg to left, pos to right

        self.ship_limit = 3 # count of ships in game (like as life?)
