import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:  # class to resource and behaviour of game

    def __init__(self):
        pygame.init()  # init game and create resource
        self.settings = Settings()  # init settings
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))  # set display size (surface)
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):  # start game
        while True:
            for event in pygame.event.get():  # wait event from keyboard or mouse (event manager)
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)  # new color by settings
            self.ship.blitme()
            pygame.display.flip()  # draw last screen (update field of fire)


if __name__ == '__main__':  # run if file called directly
    ai = AlienInvasion()
    ai.run_game()


