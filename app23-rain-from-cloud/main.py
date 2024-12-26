import os
import random
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def rain_effect(width=80, height=24, delay=0.1):
    while True:
        clear_screen()
        for _ in range(height):
            line = ''.join(random.choice([' ', '*', '#', '.']) for _ in range(width))
            print(line)
        time.sleep(delay)


if __name__ == '__main__':
    rain_effect()
