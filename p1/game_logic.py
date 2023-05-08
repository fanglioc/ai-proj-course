import pygame
from config import *

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
                elif event.key == pygame.K_UP:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
                    if new_pos[1] >= 0 and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_DOWN:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
                    if new_pos[1] < GRID_HEIGHT and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_LEFT:
                    new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
                    if new_pos[0] >= 0 and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_RIGHT:
                    new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
                    if new_pos[0] < GRID_WIDTH and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos

    def draw(self):
        # Draw the grid
        self.screen.fill(BLACK)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)
                if maze[y][x] == 1:
                    pygame.draw.rect(self.screen, WHITE, rect)
                if self.agent_pos[0] == x and self.agent_pos[1] == y:
                    if self.agent_pos[0] < 0 or self.agent_pos[0] >= GRID_WIDTH or \
                            self.agent_pos[1] < 0 or self.agent_pos[1] >= GRID_HEIGHT:
                        continue
                    pygame.draw.circle(self.screen, YELLOW, rect.center, GRID_SIZE // 2)
                if GOAL_POS[0] == x and GOAL_POS[1] == y:
                    if GOAL_POS[0] < 0 or GOAL_POS[0] >= GRID_WIDTH or \
                            GOAL_POS[1] < 0 or GOAL_POS[1] >= GRID_HEIGHT:
                        continue
                    pygame.draw.circle(self.screen, BLUE, rect.center, GRID_SIZE // 2)
                if (x, y) == GOAL_POS and (x, y) == self.agent_pos:
                    text = font.render('Bazingga!', True, PURPLE)
                    text_rect = text.get_rect(center=self.screen.get_rect().center)
                    self.screen.blit(text, text_rect)

        # Update the screen
        pygame.display.flip()

    def loop(self):
        while self.running:
            self.handle_events()
            self.draw()

        # Quit pygame
        pygame.quit()
