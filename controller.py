# controller.py
import pygame
from model import GameModel
from view import GameView

class GameController:
    def __init__(self, screen_width=1280, screen_height=720):
        pygame.init()
        pygame.display.set_caption("MVC Platformer Skeleton")

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

        self.model = GameModel(screen_width, screen_height)
        self.view = GameView(self.screen, self.model)

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # seconds per frame (if you want it)

            self._handle_events()
            self._handle_continuous_input()

            self.model.update(dt)
            self.view.draw()

        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.model.player.jump()

    def _handle_continuous_input(self):
        keys = pygame.key.get_pressed()
        player = self.model.player

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.move_left()
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.move_right()
        else:
            player.stop_horizontal()
