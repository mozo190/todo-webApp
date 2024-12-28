import random
import sys

import pygame

from classes.cloud import Cloud
from classes.lightning import Lightning

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
CLOUD_COLOR = (255, 255, 255)
TEXT_COLOR = 'yellow',
GRAVITY = 0.2
THUNDER_TIMINGS = [6000, 51000, 132000, 156000, 188000, 238000, 245000]  # Timings for thunder sound effects in milliseconds

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rain Effect')

font = pygame.font.SysFont('Arial', 13)
clock = pygame.time.Clock()
lightning = Lightning()

running = True

drops = []

drop_sounds = [pygame.mixer.Sound('assets/drop-water-1.wav'),
               pygame.mixer.Sound('assets/drop-water-2.wav'),
               pygame.mixer.Sound('assets/drop-water-3.wav'),
               pygame.mixer.Sound('assets/drop-water-4.wav'),
               pygame.mixer.Sound('assets/drop-water-5.wav'),
               pygame.mixer.Sound('assets/drop-water-6.wav')]

bg_sound = pygame.mixer.Sound('assets/background_sound.wav')


def play_drop_sound():
    random.choice(drop_sounds).play()


def handle_click(pos):
    for drop in drops[:]:
        text_surface = font.render(drop['char'], True, pygame.Color(drop['color']))
        text_rect = text_surface.get_rect(topleft=(drop['x'], drop['y']))
        if text_rect.collidepoint(pos):
            drops.remove(drop)
            break


def create_drop(cloud_rect_):
    x = random.randint(cloud_rect_.left, cloud_rect_.right)
    y = cloud_rect_.bottom
    char = random.choice([' ', '*', '#', '.', '<', '>', '^', 'v', 'x', '+', 'o', 'O', '@'])
    speed = random.randint(1, 7)
    color = random.choice(TEXT_COLOR)
    return {'x': x, 'y': y, 'char': char, 'speed': speed, 'color': color, 'alpha': 255, 'fading': False}


def check_thunder():
    current_time = pygame.time.get_ticks()
    for thunder_time in THUNDER_TIMINGS:
        if thunder_time <= current_time < thunder_time + 1000:
            lightning.trigger()
            THUNDER_TIMINGS.remove(thunder_time)  # Remove the thunder time from the list to avoid triggering it again


def main():
    cloud = Cloud(SCREEN_WIDTH // 2, 100)
    bg_sound.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event.pos)

        screen.fill(BACKGROUND_COLOR)
        check_thunder()  # Check if it's time to trigger thunder
        lightning.update(screen)  # Update lightning effect

        # Cloud drawing
        cloud.draw(screen)

        # Create drops
        if random.random() < 0.8:  # 80% chance
            drops.append(create_drop(cloud.get_rect()))

        for drop in drops[:]:  # Draw drops
            if not drop['fading']:
                drop['speed'] += GRAVITY  # Apply gravity
                drop['y'] += drop['speed']  # Move drop down

                # Check if drop hits the ground
                if drop['y'] > SCREEN_HEIGHT - 100:

                    drop['y'] = SCREEN_HEIGHT - 100  # Reset drop position
                    drop['speed'] = -drop['speed'] * 0.3  # Reverse drop speed for bouncing effect
                    play_drop_sound()  # Play drop sound
                    if abs(drop['speed']) < 1:  # If speed is too low, remove the drop
                        drop['fading'] = True  # Start fading out the drop

            # Fade out the drop
            if drop['fading']:
                drop['alpha'] -= 3  # Decrease alpha value
                if drop['alpha'] <= 0:
                    drops.remove(drop)  # Remove drop from the list if it's completely faded out

            text_surface = font.render(drop['char'], True, pygame.Color(drop['color']))
            text_surface.set_alpha(drop['alpha'])
            screen.blit(text_surface, (drop['x'], drop['y']))

        # Update the display
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
