# game.py

import pygame
from utils.characters import collision, init_characters as init_char
from utils.user_interface import user_interface
from menu import run_menu

def run_game(screen, clock):

    characters = init_char.init_characters()
    player1, player2, enemies = characters['player1'], characters['player2'], characters['enemies']
    
    running = True

    while running:
        # Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    running = False
                    run_menu(screen, clock)
                    run_game(screen, clock)

        keys = pygame.key.get_pressed()
        player1.move(keys)
        player2.move(keys)

        players = [player1, player2]
        for enemy in enemies:
            enemy.move_towards_player(players)

        # Collision Detections
        collision_detectors(player1, player2, enemies)

        is_game_over = chk_if_game_over(player1, player2)

        if(is_game_over):
            print("Gameover")
            running = False 
            run_menu(screen, clock)
            run_game(screen, clock)

        # Screen Refresh
        screen.fill((0, 0, 0))          

        # Redraw Objects
        redraw(screen, player1, player2, enemies)
    
        pygame.display.flip()
        clock.tick(60)

def collision_detectors(player1, player2, enemies):
    collision.handle_collision(player1, player2, 'player')
    
    for enemy in enemies:
        is_enemy_atk_player1 = collision.handle_collision(player1, enemy, 'enemy')
        is_enemy_atk_player2 = collision.handle_collision(player2, enemy, 'enemy')
        
    collision.handle_collision(player1, None , 'window')
    collision.handle_collision(player2, None , 'window')

def redraw(screen, player1, player2, enemies):
    # Draw Characters
    player1.draw(screen)
    player2.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    #Draw In-game UI 
    user_interface.draw_ingame_ui(screen, player1.hp, player2.hp)

def chk_if_game_over(player1, player2):
    print(player1.hp, " ", player2.hp)
    if player1.hp == 0 and player2.hp == 0:
        return True
    return False