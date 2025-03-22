
import pygame

def toggle_ingame_music():
    if not pygame.mixer.music.get_busy(): 
        print("MUSIC STARTING")
        pygame.mixer.music.load("assets/bg_music.mp3") 
        pygame.mixer.music.play(-1) 
    else:
        print("MUSIC STOPING")
        pygame.mixer.music.stop()

def run_punch_sound():
    punch_sound = pygame.mixer.Sound("assets/punch_sound_effect.mp3")
    punch_sound.play()