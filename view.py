# view.py
import pygame

BG_COLOR = (40, 40, 60)
PLAYER_COLOR = (200, 230, 70)
PLATFORM_COLOR = (100, 100, 120)

class GameView:
    def __init__(self, screen, model):
        self.screen = screen
        self.model = model
        self.font = pygame.font.SysFont("consolas", 16)

    def world_to_screen(self, rect):
        """Convert world-space rect to screen-space rect using camera offset."""
        return pygame.Rect(
            rect.x - self.model.camera_x,
            rect.y - self.model.camera_y,
            rect.width,
            rect.height,
        )

    def draw(self):
        self.screen.fill(BG_COLOR)

        # Draw platforms
        for p in self.model.level.platforms:
            screen_rect = self.world_to_screen(p)
            pygame.draw.rect(self.screen, PLATFORM_COLOR, screen_rect)

        # Draw player
        player_rect = self.world_to_screen(self.model.player.rect)
        pygame.draw.rect(self.screen, PLAYER_COLOR, player_rect)

        # Debug text for camera/player
        dbg = f"Player: {self.model.player.rect.topleft}, Cam: ({self.model.camera_x}, {self.model.camera_y})"
        txt_surface = self.font.render(dbg, True, (255, 255, 255))
        self.screen.blit(txt_surface, (8, 8))

        pygame.display.flip()
