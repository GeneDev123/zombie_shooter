import settings as st
import pygame
import random

from . import collision

class Player:
    def __init__(self, x, y, color, controls, name):
        self.name = name
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.controls = controls

        # Where the player is currently facing: [N,E,S,W,NE,NW,SE,SW]
        self.character_face_direction = [1,0,0,0,0,0,0,0]

        self.hp = st.PLAYER_HP
        self.last_damage_time = 0
        self.atk = st.PLAYER_ATK
        self.score = 0
        self.weapon = "knife"  

        self.character_image = pygame.image.load('assets/player_charater.png').convert_alpha()
        self.character_image = pygame.transform.scale(self.character_image, (self.rect.width, self.rect.height))

    def move(self, keys):   
        if self.hp > 0:
            dx, dy = 0, 0

            # Movement and direction logic
            if keys[self.controls['up']]:
                dy -= 1
            if keys[self.controls['down']]:
                dy += 1
            if keys[self.controls['left']]:
                dx -= 1
            if keys[self.controls['right']]:
                dx += 1

            # Update position
            if dx != 0 or dy != 0:
                self.character_face_direction = [0] * 8
                self.rect.x += dx * st.PLAYER_SPEED
                self.rect.y += dy * st.PLAYER_SPEED

            # Determine face direction
            self._update_character_face_direction(dx, dy)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.character_image, self.rect.topleft)

    def _update_character_face_direction(self, dx, dy):
        if dx == 1 and dy == -1:
            self.character_face_direction[4] = 1  # NE
        elif dx == -1 and dy == -1:
            self.character_face_direction[5] = 1  # NW
        elif dx == 1 and dy == 1:
            self.character_face_direction[6] = 1  # SE
        elif dx == -1 and dy == 1:
            self.character_face_direction[7] = 1  # SW
        elif dx == 0 and dy == -1:
            self.character_face_direction[0] = 1  # N
        elif dx == 1 and dy == 0:
            self.character_face_direction[1] = 1  # E
        elif dx == 0 and dy == 1:
            self.character_face_direction[2] = 1  # S
        elif dx == -1 and dy == 0:
            self.character_face_direction[3] = 1  # W
    
    def attack(self, enemies, atk_type):
        if(atk_type == "melee"):
            collision.handle_collision(self, enemies, "melee_atk")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.rect = pygame.Rect(self.set_position()[0], self.set_position()[1], 40, 40)
        self.color = st.BLACK

        self.hp = st.ENEMY_HP
        self.atk = st.ENEMY_ATK

        self.character_image = pygame.image.load('assets/zombie_character.png').convert_alpha()
        self.character_image = pygame.transform.scale(self.character_image, (self.rect.width, self.rect.height))

    def set_position(self):
        side = random.choice(['left', 'right', 'top', 'bottom'])
        if side == 'left':
            x = -40 
            y = random.randint(0, st.SCREEN_HEIGHT)
        elif side == 'right':
            x = st.SCREEN_WIDTH + 40
            y = random.randint(0, st.SCREEN_HEIGHT)
        elif side == 'top':
            x = random.randint(0, st.SCREEN_WIDTH) 
            y = -40 
        elif side == 'bottom':
            x = random.randint(0, st.SCREEN_WIDTH)
            y = st.SCREEN_HEIGHT + 40

        return x, y

    def move_towards_player(self, players):
        # Find the closest player by iterating over the list
        closest_player = min(
            (player for player in players if player.hp > 0), 
            key=lambda player: abs(self.rect.centerx - player.rect.centerx) + abs(self.rect.centery - player.rect.centery), 
            default=None
        )

        # Move towards the closest player
        if self.rect.centerx < closest_player.rect.centerx:
            self.rect.x += st.ENEMY_SPEED
        elif self.rect.centerx > closest_player.rect.centerx:
            self.rect.x -= st.ENEMY_SPEED

        if self.rect.centery < closest_player.rect.centery:
            self.rect.y += st.ENEMY_SPEED
        elif self.rect.centery > closest_player.rect.centery:
            self.rect.y -= st.ENEMY_SPEED

    def apply_damage(self, damage, fallback_direction):
        self.hp = self.hp - damage

        fallback_unit = 20
        is_dead = False

        # [N,E,S,W,NE,NW,SE,SW]
        if(fallback_direction == [1,0,0,0,0,0,0,0]):
            self.rect.top = self.rect.top - fallback_unit

        elif(fallback_direction == [0,1,0,0,0,0,0,0]):
            self.rect.right = self.rect.right + fallback_unit

        elif(fallback_direction == [0,0,1,0,0,0,0,0]):
            self.rect.top = self.rect.top + fallback_unit

        elif(fallback_direction == [0,0,0,1,0,0,0,0]):
            self.rect.right = self.rect.right - fallback_unit

        if self.hp < 1: 
            is_dead = True
        
        return is_dead


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.character_image, self.rect.topleft)

def init_characters():
    player1 = Player(
        x = st.SCREEN_WIDTH // 3,
        y = st.SCREEN_HEIGHT // 2,
        color = st.BLACK,
        controls={
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d,
        },
        name = 'player1'
    )

    player2 = Player(
        x= (st.SCREEN_WIDTH * 2) // 3,
        y= st.SCREEN_HEIGHT // 2,
        color= st.BLACK,  # Red color for Player 2
        controls={
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
        },
        name = 'player2'
    )

    enemies = [Enemy('zombie') for _ in range(3)]
    
    characters = {
        "player1": player1,
        "player2": player2,
        "enemies": enemies,
    }

    return characters
