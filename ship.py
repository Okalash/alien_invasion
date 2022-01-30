import pygame


# class for control Ship
class Ship:

    # ai_game is instance AlienInvasion
    def __init__(self, ai_game):
        self.screen = ai_game.screen  # load game screen
        self.screen_rect = ai_game.screen.get_rect()  # load game screen rectangle (for right location)

        self.image = pygame.image.load('images/ship.bmp')  # ship picture load
        self.rect = self.image.get_rect()  # ship rectangle (as size)
        self.rect.midbottom = self.screen_rect.midbottom  # every ship load from bottom center
        # run indicators
        self.moving_right = False
        self.moving_left = False

    # draw ship in current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # update current location based on run indicator
    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1