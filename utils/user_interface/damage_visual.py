import pygame
import settings as st

def render_damage_visual(attack_area):    
    pygame.draw.rect(st.SCREEN, st.RED, attack_area, 3)