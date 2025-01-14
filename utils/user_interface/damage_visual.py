import pygame
import pygame.mixer
import settings as st
import os

# def render_damage_visual(attack_area):    
#     pygame.draw.rect(st.SCREEN, st.RED, attack_area, 3)

def render_damage_visual(attack_area):
    if not pygame.mixer.music.get_busy():  # Check if music is not already playing
        pygame.mixer.music.load("assets/punch_sound_effect.mp3")  # Load your music file
        pygame.mixer.music.play(-1)  # Play music in a loop (-1)

    damage_image_path = os.path.join(st.BASE_PATH, 'assets', 'punch_effect.png')
    damage_image = pygame.image.load(damage_image_path)  # Replace with the path to your image

    damage_image = pygame.transform.scale(damage_image, (attack_area.width, attack_area.height))
    st.SCREEN.blit(damage_image, (attack_area.x, attack_area.y))
