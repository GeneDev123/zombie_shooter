import settings as st
from . import character_update as ch_update

def handle_collision(obj1, obj2, type):
    is_collided = False 
    if type == "player" and obj2 is not None:
        # Check if player collides with another object (e.g., obstacle)
        if obj1.rect.colliderect(obj2.rect):
            # print(f"{obj1.name} collided with {obj2.name}.")
            push_back(obj1.rect, obj2.rect)

            is_collided = True
    
    elif type == "enemy":
        if obj1.rect.colliderect(obj2.rect):
            # print(f"{obj1.name} collided with {obj2.name}.")

            push_back(obj1.rect, obj2.rect)
            ch_update.character_damage(obj1, "enemy")

            is_collided = True
    elif type == "window":
        # Handle collision with the window (screen boundaries)
        handle_wall_collision(obj1)
        
        is_collided = True

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

    if is_wall_collided:
        print(f"{obj.name} collided with the window walls.")