import pygame


class Game:

    def __init__(self, width: int, height: int, name: str) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.running = True
        self.screen.fill((128, 50, 50))
        pygame.display.set_caption(name)
        self.character = pygame.image.load(r"C:\Users\05lan\Desktop\Python\Gierka\assets\characters\cwel.png")
        self.character_position = [250, 250]
        self.character_movement = [False, False, False, False]

    def run_game(self) -> None:

        while self.running:
            self.screen.fill((128, 50, 50))
            self.screen.blit(self.character, self.character_position)
            self.character_position[0] += (self.character_movement[1] - self.character_movement[0]) / 5
            self.character_position[1] += (self.character_movement[3] - self.character_movement[2]) / 5

            for event in pygame.event.get():

                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.character_movement[0] = True

                    if event.key == pygame.K_d:
                        self.character_movement[1] = True

                    if event.key == pygame.K_w:
                        self.character_movement[2] = True

                    if event.key == pygame.K_s:
                        self.character_movement[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.character_movement[0] = False

                    if event.key == pygame.K_d:
                        self.character_movement[1] = False

                    if event.key == pygame.K_w:
                        self.character_movement[2] = False

                    if event.key == pygame.K_s:
                        self.character_movement[3] = False

            pygame.display.update()
