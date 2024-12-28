import pygame.time


class Lightning:
    def __init__(self):
        self.active = False
        self.start_time = 0
        self.duration = 20  # duration of the lightning in frames

    def trigger(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def update(self, surface):
        if self.active:
            surface.fill((255, 255, 255))
            if pygame.time.get_ticks() - self.start_time > self.duration:
                self.active = False
