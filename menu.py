# menu.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

def draw_menu(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)
    title = font.render("SIMPLE HORROR GAME", True, BLACK)
    start_button = font.render("Press ENTER to Start", True, BLACK)
    quit_button = font.render("Press ESC to Quit", True, BLACK)
    
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
    screen.blit(start_button, (SCREEN_WIDTH // 2 - start_button.get_width() // 2, 300))
    screen.blit(quit_button, (SCREEN_WIDTH // 2 - quit_button.get_width() // 2, 400))