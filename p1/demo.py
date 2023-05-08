import pygame

# Define the maze layout
maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

# Define the grid size and the window size
GRID_SIZE = 50
GRID_WIDTH = len(maze[0])
GRID_HEIGHT = len(maze)
width, height = GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Define the agent starting position
agent_pos = (0, 0)

# Define the goal position
goal_pos = (GRID_WIDTH-1, GRID_HEIGHT-1)

# Define the font
font = pygame.font.SysFont('Comic Sans MS', 50)

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                new_pos = (agent_pos[0], agent_pos[1]-1)
                if new_pos[1] >= 0 and not maze[new_pos[1]][new_pos[0]]:
                    agent_pos = new_pos
            elif event.key == pygame.K_DOWN:
                new_pos = (agent_pos[0], agent_pos[1]+1)
                if new_pos[1] < GRID_HEIGHT and not maze[new_pos[1]][new_pos[0]]:
                    agent_pos = new_pos
            elif event.key == pygame.K_LEFT:
                new_pos = (agent_pos[0]-1, agent_pos[1])
                if new_pos[0] >= 0 and not maze[new_pos[1]][new_pos[0]]:
                    agent_pos = new_pos
            elif event.key == pygame.K_RIGHT:
                new_pos = (agent_pos[0]+1, agent_pos[1])
                if new_pos[0] < GRID_WIDTH and not maze[new_pos[1]][new_pos[0]]:
                    agent_pos = new_pos

    # Draw the grid
    screen.fill(BLACK)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            if agent_pos[0] == x and agent_pos[1] == y:
                if agent_pos[0] < 0 or agent_pos[0] >= GRID_WIDTH or \
                   agent_pos[1] < 0 or agent_pos[1] >= GRID_HEIGHT:
                    continue
                pygame.draw.circle(screen, YELLOW, rect.center, GRID_SIZE//2)
            if goal_pos[0] == x and goal_pos[1] == y:
                if goal_pos[0] < 0 or goal_pos[0] >= GRID_WIDTH or \
                   goal_pos[1] < 0 or goal_pos[1] >= GRID_HEIGHT:
                    continue
                pygame.draw.circle(screen, BLUE, rect.center, GRID_SIZE//2)
            if (x, y) == goal_pos and (x, y) == agent_pos:
                text = font.render('Bazingga!', True, PURPLE)
                text_rect = text.get_rect(center=screen.get_rect().center)
                screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
