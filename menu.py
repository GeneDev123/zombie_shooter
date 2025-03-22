# menu.py

import pygame
import settings as st
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

def run_menu(screen, clock):
    in_menu = True
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key starts the game
                    in_menu = False

                elif event.key == pygame.K_ESCAPE:  # Escape key quits the game
                    pygame.quit()
                    return

        draw_menu(screen)
        pygame.display.flip()
        clock.tick(st.FPS)

def draw_menu(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)

    # Title
    title = font.render("SIMPLE HORROR GAME", True, BLACK)

    # Buttons
    start_button = font.render("Press ENTER to Start", True, BLACK)
    quit_button = font.render("Press ESC to Quit", True, BLACK)

    # Blit elements (properly centered)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 120))
    screen.blit(start_button, (SCREEN_WIDTH // 2 - start_button.get_width() // 2, 250))
    screen.blit(quit_button, (SCREEN_WIDTH // 2 - quit_button.get_width() // 2, 320))
