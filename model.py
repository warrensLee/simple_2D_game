# model.py
import pygame

GRAVITY = 0.4
MOVE_SPEED = 4
JUMP_SPEED = -10

class Player:
    def __init__(self, x, y, w=32, h=48):
        self.rect = pygame.Rect(x, y, w, h)
        self.vx = 0
        self.vy = 0
        self.on_ground = False

    def move_left(self):
        self.vx = -MOVE_SPEED

    def move_right(self):
        self.vx = MOVE_SPEED

    def stop_horizontal(self):
        self.vx = 0

    def jump(self):
        if self.on_ground:
            self.vy = JUMP_SPEED
            self.on_ground = False

    def apply_gravity(self):
        self.vy += GRAVITY

    def update(self, level):
        # horizontal move
        self.rect.x += self.vx
        self._handle_collisions(level.platforms, axis="x")

        # vertical move
        self.apply_gravity()
        self.rect.y += self.vy
        self.on_ground = False
        self._handle_collisions(level.platforms, axis="y")

    def _handle_collisions(self, platforms, axis):
        for p in platforms:
            if self.rect.colliderect(p):
                if axis == "x":
                    if self.vx > 0:
                        self.rect.right = p.left
                    elif self.vx < 0:
                        self.rect.left = p.right
                    self.vx = 0
                else:  # "y"
                    if self.vy > 0:
                        self.rect.bottom = p.top
                        self.on_ground = True
                    elif self.vy < 0:
                        self.rect.top = p.bottom
                    self.vy = 0


class Level:
    def __init__(self):
        # world size bigger than screen => sliding camera
        self.world_width = 3000
        self.world_height = 720

        # Simple list of static platforms in world coordinates
        self.platforms = []
        self._build_test_level()

    def _build_test_level(self):
        # ground
        self.platforms.append(pygame.Rect(0, 600, self.world_width, 120))
        # some floating platforms
        self.platforms.append(pygame.Rect(300, 500, 200, 20))
        self.platforms.append(pygame.Rect(700, 450, 200, 20))
        self.platforms.append(pygame.Rect(1200, 400, 200, 20))

    def reset(self):
        # hook for resetting level state if needed
        pass


class GameModel:
    """Root model that holds all game state."""
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.level = Level()
        self.player = Player(100, 100)

        # camera represented as top-left position in world coords
        self.camera_x = 0
        self.camera_y = 0

    def update(self, dt):
        """Update all game objects."""
        self.player.update(self.level)
        self._update_camera()

    def _update_camera(self):
        # Keep player near center of screen horizontally
        target_x = self.player.rect.centerx - self.screen_width // 2
        target_y = self.player.rect.centery - self.screen_height // 2

        # Simple hard follow (you can smooth it later if you want)
        self.camera_x = max(0, min(target_x, self.level.world_width - self.screen_width))
        self.camera_y = max(0, min(target_y, self.level.world_height - self.screen_height))
