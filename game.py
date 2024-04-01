# symple pygame program

# import and initialize the pygame library
import pygame
from settings import Settings

def run_game():
    pygame.init()
    gm_settings = Settings()

    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # run until the user asks to quit
    running = True
    while running:
        screen.fill(gm_settings.bg_color)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Flip the Display
        pygame.display.flip()
    # Done! Time to quit.
    pygame.quit()

run_game()