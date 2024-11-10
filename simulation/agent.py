# agent.py
import pygame

class Agent:
    def __init__(self, environment, x=100, y=100, speed=5):
        self.environment = environment
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 128, 255))  # Blue color for the agent
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed
        elif direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed

        # Enforce boundaries using the environment's limit_position method
        self.environment.limit_position(self.rect)
    
    def get_position(self):
        return self.rect.x, self.rect.y
