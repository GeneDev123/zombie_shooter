# game.py

import pygame
from utils.characters import collision, init_characters as init_char

def run_game(screen, clock):

    characters = init_char.init_characters()
    player1, player2, enemies = characters['player1'], characters['player2'], characters['enemies']
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player1.move(keys)
        player2.move(keys)

        players = [player1, player2]
        for enemy in enemies:
            enemy.move_towards_player(players)

        screen.fill((255, 255, 255))  # Clear screen

        redraw(screen, player1, player2, enemies)
        player1.draw(screen)
        player2.draw(screen)

        collision.handle_collision(player1, player2, 'player')
        
        for enemy in enemies:
            collision.handle_collision(player1, enemy, 'enemy')
            collision.handle_collision(player2, enemy, 'enemy')
        
        collision.handle_collision(player1, None , 'window')
        collision.handle_collision(player2, None , 'window')
        
        pygame.display.flip()
        clock.tick(60)

def redraw(screen, player1, player2, enemies):
    player1.draw(screen)
    player2.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)