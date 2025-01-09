import settings as st
import time
import pygame 

def character_damage(character, type):
    current_time = pygame.time.get_ticks()

    if type == "enemy":
        if current_time - character.last_damage_time >= 1000 and character.hp > 0:
            character.hp -= st.ENEMY_ATK
            character.last_damage_time = current_time