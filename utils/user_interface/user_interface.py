import pygame 

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, GREEN

def draw_ingame_ui(screen, player1, player2):

    font = pygame.font.Font(None, 36)
    score_font = pygame.font.Font(None, 25)

    # Player 1 Health Bar
    pygame.draw.rect(screen, RED, (50, 50, 200, 20))  # Background bar
    pygame.draw.rect(screen, GREEN, (50, 50, 2 * player1.hp, 20))  # Health bar

    # Player 2 Health Bar
    pygame.draw.rect(screen, RED, (550, 50, 200, 20))  # Background bar
    pygame.draw.rect(screen, GREEN, (550, 50, 2 * player2.hp, 20))  # Health bar

    # Labels
    player1_label = font.render("Player 1", True, WHITE)
    player2_label = font.render("Player 2", True, WHITE)
    restart_label = font.render("Press 'R' to Restart", True, WHITE)

    # Player Score
    player1_score = font.render("Score: " + str(player1.score) , True, WHITE)
    player2_score = font.render("Score: " + str(player2.score) , True, WHITE)

    # Draw labels
    screen.blit(player1_label, (50, 20))
    screen.blit(player2_label, (550, 20))
    
    screen.blit(player1_score, (50, 75))
    screen.blit(player2_score, (550, 75))
    screen.blit(restart_label, (SCREEN_WIDTH // 2 - restart_label.get_width() // 2, SCREEN_HEIGHT - 50))
