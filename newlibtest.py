import pygame
class PathFollower:
    def __init__(self, path, speed):
        """
        path: list of (x, y) tuples from Pathfinding class
        speed: movement speed in pixels per second
        """
        self.path = path
        self.speed = speed

        self.current_index = 0
        self.position = pygame.Vector2(path[0])

        self.checkpoints = set()   # {(x, y), ...}
        self.state = "moving"      # moving | stopped

    def update(self, dt):
        """
        Called every frame.
        dt = delta time in seconds.
        """
        if self.state == "moving":
            self._follow_path(dt)

    def _follow_path(self, dt):
        """
        Moves the object toward the next node in the path.
        """
        if self.current_index >= len(self.path):
            return  # Path finished

        target = pygame.Vector2(self.path[self.current_index])
        direction = target - self.position

        if direction.length() == 0:
            self._advance_path()
            return

        direction = direction.normalize()
        self.position += direction * self.speed * dt

        # Snap to node if close enough
        if self.position.distance_to(target) < 2:
            self.position = target
            self._advance_path()

    def _advance_path(self):
        """
        Advances to next node and checks checkpoints.
        """
        self.current_index += 1

        if tuple(self.position) in self.checkpoints:
            self.state = "stopped"

    def resume(self):
        """
        Resume movement after stopping.
        """
        self.state = "moving"

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, 8)
