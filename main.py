
import pygame
import pygame.mixer
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

    if not pygame.mixer.music.get_busy():  # Check if music is not already playing
        pygame.mixer.music.load("assets/bg_music.mp3")  # Load your music file
        pygame.mixer.music.play(-1)  # Play music in a loop (-1)

    run_menu(screen, clock)
    run_game(screen, clock)

if __name__ == "__main__":
    main()
