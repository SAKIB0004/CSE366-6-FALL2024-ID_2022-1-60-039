# run.py
import pygame
import sys
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame AI Simulation Framework")

# Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)

# Create environment and agent instances
environment = Environment(WINDOW_WIDTH, WINDOW_HEIGHT)
agent = Agent(environment)

# Main loop
running = True
while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        agent.move("left")
    if keys[pygame.K_RIGHT]:
        agent.move("right")
    if keys[pygame.K_UP]:
        agent.move("up")
    if keys[pygame.K_DOWN]:
        agent.move("down")

    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)

    # Draw the agent
    screen.blit(agent.image, agent.rect)

    # Display the agent's position as text
    agent_position = agent.get_position()
    position_text = font.render(f"Position: {agent_position}", True, TEXT_COLOR)
    screen.blit(position_text, (0, 0))

    # Flip the display
    pygame.display.flip()



# Quit Pygame properly
pygame.quit()
sys.exit()
