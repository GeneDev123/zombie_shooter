import settings as st
import pygame
import random

class Player:
    def __init__(self, x, y, color, controls, name):
        self.name = name
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.controls = controls

        self.hp = st.PLAYER_HP
        self.atk = st.PLAYER_ATK  

    def move(self, keys):
        if keys[self.controls['up']]:
            self.rect.y -= st.PLAYER_SPEED 
        if keys[self.controls['down']]:
            self.rect.y += st.PLAYER_SPEED
        if keys[self.controls['left']]:
            self.rect.x -= st.PLAYER_SPEED
        if keys[self.controls['right']]:
            self.rect.x += st.PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Enemy:
    def __init__(self, name):
        self.name = name
        self.rect = pygame.Rect(random.choice([-40, st.SCREEN_WIDTH]), random.choice([-40, st.SCREEN_HEIGHT]), 40, 40)
        self.color = st.GREEN

        self.hp = st.ENEMY_HP
        self.atk = st.ENEMY_ATK

    def move_towards_player(self, players):
        # Find the closest player by iterating over the list
        closest_player = min(players, key=lambda player: abs(self.rect.centerx - player.rect.centerx) + abs(self.rect.centery - player.rect.centery))

        
        # Move towards the closest player
        if self.rect.centerx < closest_player.rect.centerx:
            self.rect.x += st.ENEMY_SPEED
        elif self.rect.centerx > closest_player.rect.centerx:
            self.rect.x -= st.ENEMY_SPEED

        if self.rect.centery < closest_player.rect.centery:
            self.rect.y += st.ENEMY_SPEED
        elif self.rect.centery > closest_player.rect.centery:
            self.rect.y -= st.ENEMY_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


        
def init_characters():
    player1 = Player(
        x = st.SCREEN_WIDTH // 3,
        y = st.SCREEN_HEIGHT // 2,
        color = st.BLUE,
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
        color= st.RED,  # Red color for Player 2
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
