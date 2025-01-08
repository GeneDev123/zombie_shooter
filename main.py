
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from menu import draw_menu
from game import run_game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A SIMPLE HORROR GAME")
    clock = pygame.time.Clock()

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
        clock.tick(FPS)

    # Start the game
    run_game(screen, clock)

if __name__ == "__main__":
    main()
