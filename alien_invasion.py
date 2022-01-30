import sys
import pygame
from settings import Settings
from ship import Ship


# class to resource and behaviour of game
class AlienInvasion:

    # init game and create resource
    def __init__(self):
        pygame.init()
        self.settings = Settings()  # init settings
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))  # set display size (surface)
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    #  start game
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    # wait react for mouse or keyboard
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit from game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    # redraw screen
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # new color by settings
        self.ship.blitme()
        pygame.display.flip()  # draw last screen (update field of fire)


if __name__ == '__main__':  # run if file called directly
    ai = AlienInvasion()
    ai.run_game()
