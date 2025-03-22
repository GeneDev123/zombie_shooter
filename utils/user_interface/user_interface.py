import pygame 

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, GREEN, TILE_SIZE, TILESET

def draw_ingame_ui(screen, player1, player2):
    font = pygame.font.Font(None, 36)
    score_font = pygame.font.Font(None, 25)

    # Health bar settings
    bar_width = 200
    bar_height = 20
    bar_y = 30  # Y position for both health bars

    # Player 1 Health Bar
    pygame.draw.rect(screen, RED, (50, bar_y, bar_width, bar_height))  # Background bar
    pygame.draw.rect(screen, GREEN, (50, bar_y, max(0, (bar_width * player1.hp / 100)), bar_height))  # Health bar

    # Player 2 Health Bar
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - 50 - bar_width, bar_y, bar_width, bar_height))  # Background bar
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH - 50 - bar_width, bar_y, max(0, (bar_width * player2.hp / 100)), bar_height))  # Health bar

    # Labels
    player1_label = font.render("Player 1", True, WHITE)
    player2_label = font.render("Player 2", True, WHITE)
    restart_label = font.render("Press 'R' to Restart", True, WHITE)

    # Player Score
    player1_score = score_font.render("Score: " + str(player1.score), True, WHITE)
    player2_score = score_font.render("Score: " + str(player2.score), True, WHITE)

    # Draw labels
    screen.blit(player1_label, (50, bar_y - 25))
    screen.blit(player2_label, (SCREEN_WIDTH - 50 - player2_label.get_width(), bar_y - 25))

    # Draw scores
    screen.blit(player1_score, (50, bar_y + bar_height + 5))
    screen.blit(player2_score, (SCREEN_WIDTH - 50 - player2_score.get_width(), bar_y + bar_height + 5))

    # Restart label centered at bottom
    screen.blit(restart_label, (SCREEN_WIDTH // 2 - restart_label.get_width() // 2, SCREEN_HEIGHT - 50))

def get_tile(x, y):
    return TILESET.subsurface((x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def get_ground_tile_map():
    tilemap = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        [3, 9, 4, 4, 9, 4, 9, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9, 4, 4, 5],
        [3, 4, 4, 4, 9, 4, 4, 4, 4, 4, 9, 9, 4, 4, 4, 9, 9, 4, 4, 5],
        [3, 4, 4, 4, 9, 4, 4, 4, 9, 4, 9, 9, 4, 9, 4, 4, 4, 4, 4, 5],
        [3, 4, 4, 4, 9, 9, 4, 9, 4, 4, 9, 9, 9, 4, 4, 4, 4, 4, 4, 5],
        [3, 9, 4, 9, 4, 9, 4, 4, 4, 4, 4, 4, 9, 4, 4, 4, 9, 4, 4, 5],
        [3, 9, 4, 4, 4, 4, 9, 4, 4, 4, 4, 4, 4, 4, 9, 4, 4, 4, 4, 5],
        [3, 4, 9, 4, 4, 9, 4, 4, 4, 4, 4, 9, 4, 4, 9, 4, 4, 4, 4, 5],
        [3, 4, 4, 4, 9, 4, 4, 4, 9, 9, 4, 4, 4, 4, 9, 4, 4, 4, 9, 5],
        [3, 4, 9, 9, 4, 9, 4, 9, 4, 4, 4, 9, 4, 9, 4, 9, 4, 4, 4, 5],
        [3, 4, 4, 4, 4, 9, 4, 4, 9, 4, 4, 9, 4, 9, 4, 4, 9, 4, 4, 5],
        [3, 9, 9, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9, 4, 4, 4, 9, 4, 4, 5],
        [3, 9, 9, 4, 4, 9, 4, 4, 9, 4, 4, 4, 4, 4, 4, 9, 9, 4, 4, 5],
        [3, 9, 4, 4, 4, 9, 4, 4, 9, 4, 4, 9, 4, 9, 4, 4, 9, 9, 9, 5],
        [6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8],
    ]

    return tilemap

def get_ground_tile_position():
    tile_positions = {
        # width, height
        0: (5.5 ,1), # ground 1
        1: (6.5 ,1), # ground 2
        2: (7.5 ,1), # ground 3
        3: (5.5 ,2), # ground 4
        4: (6.5 ,2), # ground 5
        5: (7.5 ,2), # ground 6
        6: (5.5 ,3), # ground 7
        7: (6.5 ,3), # ground 8
        8: (7.5 ,3), # ground 9
        9: (8.5 ,1), # ground 10
    }
    return tile_positions

def get_ingame_background(screen):
    
    tilemap = get_ground_tile_map()
    tile_positions = get_ground_tile_position()
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            if tile in tile_positions:
                tile_x, tile_y = tile_positions[tile]
                screen.blit(get_tile(tile_x, tile_y), (col_index * TILE_SIZE, row_index * TILE_SIZE))