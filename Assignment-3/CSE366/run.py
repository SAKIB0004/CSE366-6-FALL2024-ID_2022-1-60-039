# Main Run
import random
import pygame

from environment import Environment, crossover, fitness, mutate, selection


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    font = pygame.font.Font(None, 24)
    pygame.display.set_caption("Task Assignment Visualization")

    num_slot = 8
    num_students = 5
    n_generations = 100
    population_size = 50
    environment = Environment(num_slot, num_students)
    population = environment.generate_assignments()

    best_solution = None
    best_fitness = float('inf')

    for generation in range(n_generations):
        selected = selection(population, environment)
        next_generation = []

        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            next_generation.append(mutate(child, num_students))

        population = next_generation
        current_best = min(population, key=lambda ind: fitness(ind, environment))
        current_fitness = fitness(current_best, environment)

        # Update the best solution if the current one is better
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            best_solution = current_best

        # Debugging: Print best fitness and generation
        print(f"Generation: {generation + 1}, Best Fitness: {best_fitness:.2f}")

        # Draw the grid with the best solution
        environment.draw_grid(screen, font, best_solution)
        generation_text = font.render(f"Generation: {generation + 1}", True, (0, 0, 0))
        fitness_text = font.render(f"Best Fitness: {best_fitness:.2f}", True, (0, 0, 0))
        screen.blit(generation_text, (800, 50))
        screen.blit(fitness_text, (800, 80))

        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()