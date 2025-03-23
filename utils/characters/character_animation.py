import pygame
import os
from settings import BASE_PATH, FPS, TILE_SIZE


def init_character_animation(character_type):
    if character_type == 'skeleton':
        skeleton_run_frame = []

        # Load each frame individually
        for i in range(1, 7):  # Runs from Run_1.png to Run_6.png
            frame_path = os.path.join(BASE_PATH, 'assets', 'skeleton', f'Run_{i}.png')
            frame = pygame.image.load(frame_path).convert_alpha()
            frame = pygame.transform.scale(frame, (TILE_SIZE + 16, TILE_SIZE + 16))
            skeleton_run_frame.append(frame)

        return skeleton_run_frame


    