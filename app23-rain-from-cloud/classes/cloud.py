import pygame.draw


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/cloud2.png')
        self.image = pygame.transform.scale(self.image, (400, 200))

    def draw(self, surface):
        surface.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))

    def get_rect(self):
        return pygame.Rect(self.x - self.image.get_width() // 2,
                           self.y - self.image.get_height() // 2,
                           self.image.get_width(),
                           self.image.get_height())
