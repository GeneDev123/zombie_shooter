# game.py

import pygame
from utils.characters import collision, init_characters as init_char
from utils.user_interface import user_interface
from utils.user_interface.end_game import run_end_game_page
from utils.sound.main import toggle_ingame_music
from menu import run_menu

def run_game(screen, clock):
    print("RUN GAME")
    game_settings = init_game_settings()
    characters = init_char.init_characters()
    player1, player2, enemies = characters['player1'], characters['player2'], characters['enemies']
    
    toggle_ingame_music()

    running = True
    while running:
        # Screen Refresh
        screen.fill((0, 0, 0))          

        # Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    running = False
                    toggle_ingame_music()
                    run_menu(screen, clock)
                    run_game(screen, clock)

                if event.key == pygame.K_SPACE:  
                    player1.attack(enemies, 'melee')
                    
                if event.key == pygame.K_RCTRL:  
                    player2.attack(enemies, 'melee')

        keys = pygame.key.get_pressed()
        player1.move(keys)
        player2.move(keys)

        players = [player1, player2]
        for enemy in enemies:
            enemy.move_towards_player(players)

        current_time = pygame.time.get_ticks()

        if current_time - game_settings['last_time_enemy_spawn'] >= game_settings['interval']:
            print(game_settings)
            game_settings['last_time_enemy_spawn'] = current_time
            enemies = enemies + [init_char.Enemy('zombie') for _ in range(1 + game_settings['enemies_respawn_count'])]
            game_settings['enemies_respawn_count'] += 1

        # Collision Detections
        collision_detectors(player1, player2, enemies)

        is_game_over = chk_if_game_over(player1, player2)
        if(is_game_over):
            running = False 
            run_end_game_page(screen, clock, {'player1': player1, 'player2': player2})
            toggle_ingame_music()
            run_menu(screen, clock)
            run_game(screen, clock)

        # Redraw Objects
        redraw(screen, player1, player2, enemies)
    
        pygame.display.flip()
        clock.tick(60)

def init_game_settings():
    game_settings = {
        "enemies_respawn_count": 0, 
        "last_time_enemy_spawn": 0, 
        "interval": 15000 # 15 sec
    }
    return game_settings

def collision_detectors(player1, player2, enemies):
    collision.handle_collision(player1, player2, 'player')
    
    for enemy in enemies:
        is_enemy_atk_player1 = collision.handle_collision(player1, enemy, 'enemy')
        is_enemy_atk_player2 = collision.handle_collision(player2, enemy, 'enemy')

    for i in range(0, len(enemies)):
        for j in range(i, len(enemies)):
            collision.handle_collision(enemies[i], enemies[j], 'enemy-to-enemy')
            
    collision.handle_collision(player1, None , 'window')
    collision.handle_collision(player2, None , 'window')

def redraw(screen, player1, player2, enemies):
    user_interface.get_ingame_background(screen)
    
    # Draw Characters
    player1.draw(screen)
    player2.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    #Draw In-game UI 
    user_interface.draw_ingame_ui(screen, player1, player2)

def chk_if_game_over(player1, player2):
    if player1.hp == 0 and player2.hp == 0:
        return True
    return False