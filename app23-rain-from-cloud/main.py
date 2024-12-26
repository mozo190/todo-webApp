import random
import sys

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
CLOUD_COLOR = (255, 255, 255)
TEXT_COLOR = yellow = (255, 255, 0)
CLOUD_RADIUS = 100
GRAVITY = 0.5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rain Effect')

font = pygame.font.SysFont('Arial', 10)

cloud_rect = pygame.Rect(SCREEN_WIDTH // 2 - CLOUD_RADIUS, 50, CLOUD_RADIUS * 2,
                         CLOUD_RADIUS * 2)

clock = pygame.time.Clock()

running = True

drops = []


def create_drop():
    x = random.randint(cloud_rect.left, cloud_rect.right)
    y = cloud_rect.bottom
    char = random.choice([' ', '*', '#', '.', '<', '>', '^', 'v', 'x', '+', 'o', 'O', '@'])
    speed = random.randint(1, 7)
    return {'x': x, 'y': y, 'char': char, 'speed': speed, 'alpha': 255, 'fading': False}


def main():
    clock_rain = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(screen, CLOUD_COLOR, cloud_rect.center, CLOUD_RADIUS)

        if random.random() < 0.3:  # 30% chance
            drops.append(create_drop())

        for drop in drops[:]:  # Draw drops
            if not drop['fading']:
                drop['speed'] += GRAVITY  # Apply gravity
                drop['y'] += drop['speed']  # Move drop down

                # Check if drop hits the ground
                if drop['y'] > SCREEN_HEIGHT - 100:
                    drop['y'] = SCREEN_HEIGHT - 100  # Reset drop position
                    drop['speed'] = -drop['speed'] * 0.6  # Reverse drop speed for bouncing effect
                    if abs(drop['speed']) < 1:  # If speed is too low, remove the drop
                        drop['fading'] = True  # Start fading out the drop

            # Fade out the drop
            if drop['fading']:
                if drop['alpha'] > 0:
                    drop['alpha'] -= 2  # Decrease alpha value
                else:
                    drops.remove(drop)  # Remove drop from the list if it's completely faded out

            text_surface = font.render(drop['char'], True, TEXT_COLOR)
            text_surface.set_alpha(drop['alpha'])
            screen.blit(text_surface, (drop['x'], drop['y']))

        pygame.display.flip()
        clock_rain.tick(30)


if __name__ == '__main__':
    main()
