import pygame
import settings as st
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

def run_end_game_page(screen, clock, players): 
    in_endgame = True

    while in_endgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    in_endgame = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                
        draw_endgame(screen, players)
        pygame.display.flip()
        clock.tick(st.FPS)
    
def draw_endgame(screen, players):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)

    player1 = players['player1']
    player2 = players['player2']

    page_label = font.render("YOU'RE DEAD!", True, BLACK)
    score_label = font.render('Score:', True, BLACK)
    p1_label = font.render("Player 1: " + str(player1.score), True, BLACK)
    p2_label = font.render("Player 2: " + str(player2.score), True, BLACK)
    
    start_button = font.render("Press ENTER to Start", True, BLACK)
    quit_button = font.render("Press ESC to Quit", True, BLACK)
    
    screen.blit(page_label, (SCREEN_WIDTH // 2 - page_label.get_width() // 2, 200))

    screen.blit(score_label, (SCREEN_WIDTH // 3 - p1_label.get_width() // 2, 270))
    screen.blit(p1_label, (SCREEN_WIDTH // 3 - p1_label.get_width() // 2, 320))
    screen.blit(p2_label, (SCREEN_WIDTH // 3 - p2_label.get_width() // 2 + 200, 320))

    screen.blit(start_button, (SCREEN_WIDTH // 2 - start_button.get_width() // 2, 400))
    screen.blit(quit_button, (SCREEN_WIDTH // 2 - quit_button.get_width() // 2, 460))