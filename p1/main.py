import pygame
import game_logic

# Initialize pygame
pygame.init()

# Game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Run the game loop
    game_logic.game_loop()

# Quit the game
pygame.quit()
