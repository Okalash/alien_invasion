import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


# class to resource and behaviour of game
class AlienInvasion:

    # init game and create resource
    def __init__(self):
        pygame.init()
        self.settings = Settings()  # init settings

        # fullscreen game mode
        if False:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # set display size (surface)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        # screen size from settings
        if True:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    #  start game
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()

    # wait react for mouse or keyboard
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit from game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._chech_keyup_events(event)

    # reaction to pressed key
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # if turn ESCAPE - game off
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        # shot
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    # reaction to unpressed key
    def _chech_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # delete old bullet
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    # redraw screen
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # new color by settings
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()  # draw last screen (update field of fire)

    # new bullet and add to group bullets
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # create a fleet aliens
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        avialable_space_x = self.settings.screen_width - (2 * alien_width)
        number_alines_x = avialable_space_x // (2 * alien_width)

        # create first line of aliens
        for alien_number in range(number_alines_x):
            self._create_alien(alien_number)

    # create alien and add to line
    def _create_alien(self, alien_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)



# run if file called directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
