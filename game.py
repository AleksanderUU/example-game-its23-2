# symple pygame program

# import and initialize the pygame library
import pygame
from settings import Settings
from player import Player
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
    # Instatiate player
    player = Player(screen)

    # Run until the user asks to quit
    while True:
        gf.check_events(player)
        player.update()
        gf.update_screen(gm_settings, screen, player)
        
run_game()