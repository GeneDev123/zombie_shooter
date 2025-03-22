import pygame
import settings as st
import os

from utils.sound.main import run_punch_sound

def render_damage_visual(attack_area):
    run_punch_sound()
    damage_image_path = os.path.join(st.BASE_PATH, 'assets', 'punch_effect.png')
    damage_image = pygame.image.load(damage_image_path)  # Replace with the path to your image

    damage_image = pygame.transform.scale(damage_image, (attack_area.width, attack_area.height))
    st.SCREEN.blit(damage_image, (attack_area.x, attack_area.y))
