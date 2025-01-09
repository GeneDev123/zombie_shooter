
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from menu import draw_menu, run_menu
from game import run_game
import settings

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    settings.set_screen(screen)
    pygame.display.set_caption("A SIMPLE HORROR GAME")
    clock = pygame.time.Clock()

    run_menu(screen, clock)
    run_game(screen, clock)

if __name__ == "__main__":
    main()
