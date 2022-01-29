import sys
import pygame


class AlienInvasion:  # class to resource and behaviour of game

    def __init__(self):
        pygame.init()  # init game and create resource
        self.screen = pygame.display.set_mode((1200, 800)) #set display size (surface)
        pygame.display.set_caption('Alien Invasion')

    def run_game(self): #start game
        while True:
            for event in pygame.event.get(): #wait event from keyboard or mouse
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
