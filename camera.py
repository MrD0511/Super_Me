import pygame

class Camera():
    def __init__(self, width, height, screen_width, screen_height):
        """
        Initialize the camera.
        
        :param width: Total width of the game world.
        :param height: Total height of the game world.
        :param screen_width: Width of the visible screen (viewport).
        :param screen_height: Height of the visible screen (viewport).
        """
        # Camera rectangle representing the viewable area
        self.camera = pygame.Rect(0, 0, width, height)
        
        # These additional rects are defined but not used in this snippet (could be for future extensions)
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.camera_viewport = pygame.Rect(0, 0, width, height)

        # Store screen dimensions for calculations
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height

    def apply(self, entity):
        """
        Adjusts the position of an entity to align with the camera's view.
        
        :param entity: Any game object with a `rect` attribute.
        :return: The adjusted rectangle position for rendering on the screen.
        """
        return entity.rect.move(self.camera.topleft)  # Moves entity relative to the camera's top-left corner

    def update(self, target):
        """
        Updates the camera position based on the target's position (e.g., player).
        
        :param target: The object (usually the player) that the camera follows.
        """
        # Center the camera on the target
        x = -target.rect.centerx + int(self.SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(self.SCREEN_HEIGHT / 2)

        # Prevent the camera from moving out of the left and top bounds (world's top-left corner)
        x = min(0, x)
        y = min(0, y)

        # Prevent the camera from moving beyond the right and bottom bounds of the game world
        x = max(-(self.camera.width - self.SCREEN_WIDTH), x)
        y = max(-(self.camera.height - self.SCREEN_HEIGHT), y)

        # Update the camera position with the new values
        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)
