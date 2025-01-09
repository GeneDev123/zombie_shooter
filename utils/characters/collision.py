import pygame
import settings as st
from . import character_update as ch_update
from utils.user_interface import damage_visual

def handle_collision(obj1, obj2, type):
    is_collided = False 
    if type == "player" and obj2 is not None:
        # Check if player collides with another object (e.g., obstacle)
        if obj1.rect.colliderect(obj2.rect):
            push_back(obj1.rect, obj2.rect)

            is_collided = True
    
    elif type == "enemy":
        if obj1.rect.colliderect(obj2.rect):
            push_back(obj1.rect, obj2.rect)
            ch_update.character_damage(obj1, "enemy")

            is_collided = True

    elif type == "enemy-to-enemy":
        if obj1.rect.colliderect(obj2.rect):
            push_back(obj1.rect, obj2.rect)
            is_collided = True

    elif type == "window":
        # Handle collision with the window (screen boundaries)
        handle_wall_collision(obj1)

    elif type == "melee_atk":
        # Check if meele attack collided with enemy
        handle_meele_attack(obj1, obj2)

    return is_collided

def push_back(obj1, obj2):
    if obj1.right > obj2.left and obj1.left < obj2.left:
        obj1.right = obj2.left  # Push obj1 to the left
    elif obj1.left < obj2.right and obj1.right > obj2.right:
        obj1.left = obj2.right  # Push obj1 to the right

    if obj1.bottom > obj2.top and obj1.top < obj2.top:
        obj1.bottom = obj2.top  # Push obj1 upwards
    elif obj1.top < obj2.bottom and obj1.bottom > obj2.bottom:
        obj1.top = obj2.bottom  # Push obj1 downwards

def handle_wall_collision(obj):
    screen_width, screen_height = st.SCREEN_WIDTH, st.SCREEN_HEIGHT

    is_wall_collided = False
    # Prevent the object from moving out of the left or right side of the screen
    if obj.rect.left < 0:
        obj.rect.left = 0
        is_wall_collided = True
    elif obj.rect.right > screen_width:
        obj.rect.right = screen_width
        is_wall_collided = True

    # Prevent the object from moving out of the top or bottom side of the screen
    if obj.rect.top < 0:
        obj.rect.top = 0
        is_wall_collided = True
    elif obj.rect.bottom > screen_height:
        obj.rect.bottom = screen_height
        is_wall_collided = True

def handle_meele_attack(player, enemies):
    attack_direction = tuple(player.character_face_direction)

    # Mapping of directions to their respective offsets
    direction_offsets = {
        (1, 0, 0, 0, 0, 0, 0, 0): (0, -40),  # North
        (0, 1, 0, 0, 0, 0, 0, 0): (40, 0),   # East
        (0, 0, 1, 0, 0, 0, 0, 0): (0, 40),   # South
        (0, 0, 0, 1, 0, 0, 0, 0): (-40, 0),  # West
        (0, 0, 0, 0, 1, 0, 0, 0): (40, -40), # Northeast
        (0, 0, 0, 0, 0, 1, 0, 0): (-40, -40),# Northwest
        (0, 0, 0, 0, 0, 0, 1, 0): (40, 40),  # Southeast
        (0, 0, 0, 0, 0, 0, 0, 1): (-40, 40), # Southwest
    }
    
    attack_offset = direction_offsets.get(attack_direction, (0, 0))
    attack_area = pygame.Rect(
        player.rect.x + attack_offset[0],
        player.rect.y + attack_offset[1],
        player.rect.width,
        player.rect.height
    )
    
    damage_visual.render_damage_visual(attack_area)

    for target in enemies[:]: 
        if target.name == "zombie" and attack_area.colliderect(target.rect):
            is_dead = target.apply_damage(player.atk, player.character_face_direction)
            
            if is_dead:
                player.score += 1
                enemies.remove(target)
                