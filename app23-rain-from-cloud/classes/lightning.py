import pygame.time


class Lightning:
    def __init__(self):
        self.pattern = []  # Pattern of lightning bolts
        self.current_flash = 0  # Current flash index
        self.start_time = 0  # Time when the current flash started

    def trigger(self):
        # Pattern of lightning bolts
        self.pattern = [
            (255, 200),  # Strong flash
            (150, 100),  # Weak flash
            (200, 150),  # Medium flash
            (100, 50),  # Weak flash
        ]
        self.current_flash = 0
        self.start_time = pygame.time.get_ticks()

    def update(self, surface):
        if self.current_flash < len(self.pattern):
            intensity, duration = self.pattern[self.current_flash]
            elapsed = pygame.time.get_ticks() - self.start_time
            if elapsed < duration:
                # White layer to simulate lightning
                overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
                overlay.fill((255, 255, 255, intensity))
            else:
                # Step to the next flash
                self.current_flash += 1
                self.start_time = pygame.time.get_ticks()
