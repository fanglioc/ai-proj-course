import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Agent Game")

# Set the clock
clock = pygame.time.Clock()

# Define the agent and goal positions
agent_pos = [50, 50]
goal_pos = [700, 500]

# Define the wall positions and dimensions
wall_list = [
    [300, 100, 200, 20],
    [200, 300, 20, 200],
    [500, 300, 20, 200],
    [100, 500, 600, 20]
]

# Define the font for the win message
font = pygame.font.Font(None, 80)

# Define a function to check for collisions
def check_collisions(rect1, rect2):
    if (rect1[0] < rect2[0] + rect2[2] and
        rect1[0] + rect1[2] > rect2[0] and
        rect1[1] < rect2[1] + rect2[3] and
        rect1[1] + rect1[3] > rect2[1]):
        return True
    else:
        return False

# Game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the background color
    screen.fill(BLACK)

    # Draw the walls on the screen
    for wall in wall_list:
        pygame.draw.rect(screen, WHITE, wall)

    # Draw the agent on the screen
    pygame.draw.circle(screen, YELLOW, agent_pos, 20)

    # Draw the goal on the screen
    pygame.draw.circle(screen, BLUE, goal_pos, 20)

    # Move the agent when arrow keys are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and agent_pos[0] > 0:
        agent_pos[0] -= 5
    elif keys[pygame.K_RIGHT] and agent_pos[0] < SCREEN_WIDTH:
        agent_pos[0] += 5
    elif keys[pygame.K_UP] and agent_pos[1] > 0:
        agent_pos[1] -= 5
    elif keys[pygame.K_DOWN] and agent_pos[1] < SCREEN_HEIGHT:
        agent_pos[1] += 5

    # Check for collisions between the agent and walls
    agent_rect = pygame.Rect(agent_pos[0]-20, agent_pos[1]-20, 40, 40)
    for wall in wall_list:
        wall_rect = pygame.Rect(wall)
        if check_collisions(agent_rect, wall_rect):
            if keys[pygame.K_LEFT]:
                agent_pos[0] += 5
            elif keys[pygame.K_RIGHT]:
                agent_pos[0] -= 5
            elif keys[pygame.K_UP]:
                agent_pos[1] += 5
            elif keys[pygame.K_DOWN]:
                agent_pos[1] -= 5

    # Check for collisions between the agent and goal
    goal_rect = pygame.Rect(goal_pos[0]-20, goal_pos[1]-20, 40, 40)
    if check_collisions(agent_rect, goal_rect):
        # Display the win message
        win_text = font.render("You Win!", True, BLUE)
        win_rect = win_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(win_text, win_rect)

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
