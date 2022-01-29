import pygame


class Ship:

    def __init__(self, ai_game):  # ai_game is instance AlienInvasion
        self.screen = ai_game.screen  # load game screen
        self.screen_rect = ai_game.screen.get_rect()  # load game screen rectangle (for right location)

        self.image = pygame.image.load('images/ship.bmp')  # ship picture load
        self.rect = self.image.get_rect()  # ship rectangle (as size)
        self.rect.midbottom = self.screen_rect.midbottom  # every ship load from bottom center

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # draw ship in current location

