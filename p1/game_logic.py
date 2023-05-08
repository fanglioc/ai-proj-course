import pygame
import config

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

# Draw the walls on the screen
def draw_walls():
    for wall in config.WALL_LIST:
        pygame.draw.rect(screen, config.WHITE, wall)

# Draw the agent on the screen
def draw_agent():
    pygame.draw.circle(screen, config.YELLOW, config.AGENT_POS, 20)

# Draw the goal on the screen
def draw_goal():
    pygame.draw.circle(screen, config.BLUE, config.GOAL_POS, 20)

# Draw the movable locations on the screen
def draw_movable_locations():
    for y in range(40, SCREEN_HEIGHT, 40):
        for x in range(40, SCREEN_WIDTH, 40):
            rect = pygame.Rect(x-2, y-2, 4, 4)
            if rect.collidelist(config.WALL_LIST) == -1:
                pygame.draw.rect(screen, config.PURPLE, rect)

# Move the agent
def move_agent(keys):
    if keys[pygame.K_LEFT] and config.AGENT_POS[0] > 0:
        config.AGENT_POS[0] -= 5
    elif keys[pygame.K_RIGHT] and config.AGENT_POS[0] < SCREEN_WIDTH:
        config.AGENT_POS[0] += 5
    elif keys[pygame.K_UP] and config.AGENT_POS[1] > 0:
        config.AGENT_POS[1] -= 5
    elif keys[pygame.K_DOWN] and config.AGENT_POS[1] < SCREEN_HEIGHT:
        config.AGENT_POS[1] += 5

# Check for collisions between the agent and walls
def check_wall_collisions(keys):
    agent_rect = pygame.Rect(config.AGENT_POS[0]-20, config.AGENT_POS[1]-20, 40, 40)
    for wall in config.WALL_LIST:
        wall_rect = pygame.Rect(wall)
        if check_collisions(agent_rect, wall_rect):
            if keys[pygame.K_LEFT]:
                config.AGENT_POS[0] += 5
            elif keys[pygame.K_RIGHT]:
                config.AGENT_POS[0] -= 5
            elif keys[pygame.K_UP]:
                config.AGENT_POS[1] += 5
            elif keys[pygame.K_DOWN]:
                config.AGENT_POS[1] -= 5

# Game loop
def game_loop():
    # Set the background color
    screen.fill(config.BLACK)

    # Draw the walls on the screen
    draw_walls()

    # Draw the agent on the screen
    draw_agent()

    # Draw the goal on the screen
    draw_goal()

    # Draw the movable locations on the screen
    draw_movable_locations()

    # Move the agent when arrow keys are pressed
    keys = pygame.key.get_pressed()
    move_agent(keys)

    # Check for collisions between the agent and walls
    check_wall_collisions(keys)

    # Check for collisions between the agent and goal
    goal_rect = pygame.Rect(config.GOAL_POS[0]-20, config.GOAL_POS[1]-20, 40, 40)
    agent_rect = pygame.Rect(config.AGENT_POS[0]-20, config.AGENT_POS[1]-20, 40, 40)
    if check_collisions(agent_rect, goal_rect):
        # Display the win message
        win_text = font.render("You Win!", True, config.BLUE)
        win_rect = win_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(win_text, win_rect)

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
