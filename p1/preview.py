import pygame
from config import *
from path_planning import astar

# Initialize pygame
pygame.init()

# Define the font
font = pygame.font.SysFont(FONT, FONT_SIZE)

class Game:
    def __init__(self):
        # Set up the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Game")

        # Define the agent starting position
        self.agent_pos = AGENT_POS

        # Define the game loop
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self):
        # Draw the grid
        self.screen.fill(BLACK)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)
                if maze[y][x] == 1:
                    pygame.draw.rect(self.screen, WHITE, rect)
                if GOAL_POS[0] == x and GOAL_POS[1] == y:
                    if GOAL_POS[0] < 0 or GOAL_POS[0] >= GRID_WIDTH or \
                            GOAL_POS[1] < 0 or GOAL_POS[1] >= GRID_HEIGHT:
                        continue
                    pygame.draw.circle(self.screen, BLUE, rect.center, GRID_SIZE // 2)

        # Draw the agent
        agent_rect = pygame.Rect(self.agent_pos[0] * GRID_SIZE, self.agent_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        if self.agent_pos[0] < 0 or self.agent_pos[0] >= GRID_WIDTH or \
                self.agent_pos[1] < 0 or self.agent_pos[1] >= GRID_HEIGHT:
            pass
        else:
            pygame.draw.circle(self.screen, YELLOW, agent_rect.center, GRID_SIZE // 2)

        # Update the screen
        pygame.display.flip()
        pygame.display.update()

    def run(self):
        while self.running:
            # Handle events
            self.handle_events()

            # Draw the game
            self.draw()

        # Quit pygame
        pygame.quit()

game = Game()
game.run()
