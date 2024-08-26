import sys

import pygame

from utils import load_image
from entieties import PhysicsEntity


class Game:
    def __init__(self, width, height, title):

        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        pygame.display.set_caption(self.title)

        self.display = pygame.Surface((self.width / 2, self.height / 2))

        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        self.movement = [False, False]
        self.assets = {
                'player': load_image('player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (32, 32))

    def run_game(self):
        while True:
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, (self.width, self.height)), (0, 0))
            pygame.display.update()
