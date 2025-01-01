# Environment: Defines the scheduling problem
import random
import numpy as np
import pygame


class Environment:
    def __init__(self, num_slot, num_students):
        self.num_slot = num_slot
        self.num_students = num_students
        self.slot_durations = np.random.randint(1, 2, size=num_slot)
        self.slot_priorities = np.random.randint(1, 5, size=num_slot)
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        self.students_days = [random.choices(self.days) for _ in range(num_students)]  # Randomly assign day preferences for each student

    def generate_assignments(self):
        """
        Randomly assign slot to students for initial population in the genetic algorithm.
        """
        return [np.random.randint(0, self.num_students, size=self.num_slot) for _ in range(50)]

    def draw_grid(self, screen, font, slot_assignments):
        """
        Draw a grid representing the slot assignments on the Pygame screen.
        Each row is a student, each column is a slot, colors are based on task durations, and annotations
        show task priorities and durations inside the grid.
        """
        screen.fill((255, 255, 255))  # Background color
        color_map = [(0, 0, 255 - i * 25) for i in range(10)]  # Color gradient for durations
        cell_size = 60
        margin_left = 150
        margin_top = 100

        # Display task names on the top (X-axis labels)
        for col in range(self.num_slot):
            Slot_text = font.render(f"Slot {col + 1}", True, (0, 0, 0))
            screen.blit(Slot_text, (margin_left + col * cell_size + cell_size // 3, margin_top - 30))

        # Draw each student row with tasks assigned
        for row in range(self.num_students):
            # Display student day preferences on the left of each row
            preference_text = font.render(f" {', '.join(self.students_days[row])}", True, (0, 0, 0))
            screen.blit(preference_text, (10, margin_top + row * cell_size + cell_size // 3))

            for col in range(self.num_slot):
                # Determine if this task is assigned to the current student
                assigned_student = slot_assignments[col]
                
                # Set color based on task duration
                color = color_map[self.slot_durations[col] - 1] if assigned_student == row else (200, 200, 200)
                
                # Draw the cell
                cell_rect = pygame.Rect(
                    margin_left + col * cell_size,
                    margin_top + row * cell_size,
                    cell_size,
                    cell_size
                )
                pygame.draw.rect(screen, color, cell_rect)
                pygame.draw.rect(screen, (0, 0, 0), cell_rect, 1)  # Draw cell border

                # Display task priority and duration within the cell
                priority_text = font.render(f"P{self.slot_priorities[col]}", True, (255, 255, 255) if assigned_student == row else (0, 0, 0))
                duration_text = font.render(f"{self.slot_durations[col]}h", True, (255, 255, 255) if assigned_student == row else (0, 0, 0))
                screen.blit(priority_text, (cell_rect.x + 5, cell_rect.y + 5))
                screen.blit(duration_text, (cell_rect.x + 5, cell_rect.y + 25))


# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.1
n_generations = 100

def fitness(individual, environment):
    """
    Calculate the fitness of an individual based on conflict minimization and preference alignment.
    
    Fitness = Conflict Penalty + Preference Penalty
    Lower fitness values indicate better schedules.
    """
    conflict_penalty = 0
    preference_penalty = 0

    for slot, student_id in enumerate(individual):
        # Determine the day of the week for the current slot
        day_of_slot = environment.days[slot % len(environment.days)]

        # Check for conflicts (student unavailable on this day)
        if day_of_slot not in environment.students_days[student_id]:
            conflict_penalty += 1

        # Calculate preference penalty if the day is not preferred
        if day_of_slot not in environment.students_days[student_id]:
            preference_penalty += 1

    # Combine penalties to compute total fitness
    total_fitness = conflict_penalty + preference_penalty
    return total_fitness


def selection(population, environment):
    return sorted(population, key=lambda ind: fitness(ind, environment))[:population_size // 2]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return np.concatenate([parent1[:point], parent2[point:]])

def mutate(individual, num_students):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, num_students - 1)
    return individual
