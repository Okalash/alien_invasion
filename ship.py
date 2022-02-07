import pygame
from pygame.sprite import Sprite

# class for control Ship
class Ship(Sprite):

    def __init__(self, ai_game):  # ai_game is instance AlienInvasion
        super().__init__()
        self.screen = ai_game.screen  # load game screen
        self.screen_rect = ai_game.screen.get_rect()  # load game screen rectangle (for right location)
        self.setting = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')  # ship picture load
        self.rect = self.image.get_rect()  # ship rectangle (as size)
        self.rect.midbottom = self.screen_rect.midbottom  # every ship load from bottom center

        # float value of coordinates (speed in 1.5)
        self.x = float(self.rect.x)
        # run indicators
        self.moving_right = False
        self.moving_left = False

    # draw ship in current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # update current location based on run indicator
    def update(self):
        # movement only in the screen area
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        #  update rect from self.x
        self.rect.x = self.x

    # move ship to center
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)