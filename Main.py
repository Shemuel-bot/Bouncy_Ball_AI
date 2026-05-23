"""
Genetic algorithm to evolve Ball_Trap_Brain instances to produce desired outputs.

This module runs a genetic algorithm that evolves a population of brains over
multiple generations. Each brain is evaluated against test cases, and the best
performer is mutated to create the next generation.
"""

from Ball_Brain import Ball_Trap_Brain
import Evaluation
import copy
import difflib
from Dataset import test_cases

# Test cases: pairs of (input_string, expected_output_string) used for fitness evaluation

alphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '-']  # Define the alphabet used in the brains

def main():
    """
    Run the genetic algorithm for evolving Ball_Trap_Brain instances.
    
    Returns:
        Ball_Trap_Brain: The best brain found after evolution.
    """
    # Evolution hyperparameters
    generations = 10000
    population_size = 100

    # Initialize population with random brains
    # Parameters: 10 deflectors, 2 bounce energy, alphabet of 6 characters
    population = [Ball_Trap_Brain(100, 3, alphabet, holes_multiplier=2) for _ in range(population_size)]
    best_individual = None

    # Run evolution loop
    for generation in range(generations):
        
        # Evaluate all brains and find the best performer
        best_fitness, best_individual = Evaluation.evaluate_population(population, test_cases)

        # Check for perfect solution
        if best_fitness == 1.0:
            print(f"Generation {generation}: Solution found!")
            break

        # Create next generation by mutating the best brain multiple times
        new_population = [copy.deepcopy(best_individual).Mutate(0.9, 0.025) for _ in range(population_size)]
        population = new_population
        print(f"Generation {generation}: Best fitness = {best_fitness}")
    
    return best_individual

# Run the genetic algorithm and store the best evolved brain
brain = main()
while True:
    i = input("Input some text: ")
    print(f"output: {''.join(brain.compute_input(i))}")
