# symple pygame program

# import and initialize the pygame library
import pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([800, 500])

# run until the user asks to quit
running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Flip the Display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()