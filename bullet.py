import pygame
from pygame.sprite import Sprite


# class to control bullet from ship
class Bullet(Sprite):

    def __init__(self, ai_game):  # ai_game is instance AlienInvasion
        super().__init__()  # for inheritance Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create rectangle bullet from (0,0) to middle position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.screen_height)  # build bullet
        self.rect.midtop = ai_game.ship.rect.midtop

        # save the position of bullet as float value
        self.y = float(self.rect.y)

    # control position bullet
    def update(self):
        # make a bullet over the ship
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    # draw the bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)