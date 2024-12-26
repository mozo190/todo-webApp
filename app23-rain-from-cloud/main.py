import random
import time

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


def rain_effect(width=80, height=24, delay=0.1):
    while True:
        clear_screen()
        for _ in range(height):
            line = ''.join(random.choice([' ', '*', '#', '.']) for _ in range(width))
            print(line)
        time.sleep(delay)


if __name__ == '__main__':
    rain_effect()
