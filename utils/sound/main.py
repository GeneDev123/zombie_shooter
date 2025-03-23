
import pygame
import os
from settings import BASE_PATH

def toggle_ingame_music():
    if not pygame.mixer.music.get_busy(): 
        pygame.mixer.music.load(os.path.join(BASE_PATH, 'assets', 'sound', 'bg_music.mp3')) 
        pygame.mixer.music.play(-1) 
    else:
        pygame.mixer.music.stop()

def run_punch_sound():
    punch_sound = pygame.mixer.Sound(os.path.join(BASE_PATH, 'assets', 'sound', 'punch_sound_effect.mp3'))
    punch_sound.play()