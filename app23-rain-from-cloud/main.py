import random
import sys

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
CLOUD_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)
CLOUD_RADIUS = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rain Effect')

font = pygame.font.SysFont('Arial', 30)

cloud_rect = pygame.Rect(SCREEN_WIDTH // 2 - CLOUD_RADIUS, SCREEN_HEIGHT // 2 - CLOUD_RADIUS, CLOUD_RADIUS * 2,
                         CLOUD_RADIUS * 2)

clock = pygame.time.Clock()

running = True

drops = []


def create_drop():
    x = random.randint(cloud_rect.left, cloud_rect.right)
    y = cloud_rect.bottom
    char = random.choice([' ', '*', '#', '.', '<', '>', '^', 'v', 'x', '+', 'o', 'O', '@'])
    speed = random.randint(3, 7)
    return {'x': x, 'y': y, 'char': char, 'speed': speed}


def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(screen, CLOUD_COLOR, cloud_rect.center, CLOUD_RADIUS)

        if random.random() < 0.3:  # 30% chance
            drops.append(create_drop())

        for drop in drops:  # Draw drops
            drop['y'] += drop['speed']  # Move drop down
            if drop['y'] > SCREEN_HEIGHT:  # Drop is out of screen
                drops.remove(drop)
            else:
                text_surface = font.render(drop['char'], True, TEXT_COLOR)
                screen.blit(text_surface, (drop['x'], drop['y']))

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
