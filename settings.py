# settings.py

import sys
import os
import pygame

if getattr(sys, 'frozen', False):  # Check if the program is bundled
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(__file__)

# # Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

TILE_SIZE = 32
TILESET =  pygame.image.load(os.path.join(BASE_PATH, 'assets', 'tile_set.png'))

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Frames per second
FPS = 60
ANIMATION_DELAY = 6

# Character settings
PLAYER_SPEED = 3
PLAYER_HP = 100
PLAYER_ATK = 10

ENEMY_SPEED = 1
ENEMY_HP = 30
ENEMY_ATK = 10

SCREEN = None

def set_screen(screen):
    global SCREEN 
    SCREEN = screen