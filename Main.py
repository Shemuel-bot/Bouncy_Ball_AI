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

# Test cases: pairs of (input_string, expected_output_string) used for fitness evaluation
test_cases = [('#a', 'a'), ('#b', 'b'), ('#c', 'c'), 
              ('#d', 'd'), ('#e', 'e'), ('#f', 'f'), 
              ('#g', 'g'), ('#h', 'h'), ('#i', 'i'),
              ('#aa', 'aa'), ('#bb', 'bb'), ('#cc', 'cc'),
              ('#dd', 'dd'), ('#ee', 'ee'), ('#ff', 'ff'),
              ('#gg', 'gg'), ('#hh', 'hh'), ('#ii', 'ii'),
              ('#abc', 'abc'), ('#def', 'def'), ('#ghi', 'ghi'),
              ('#aaa', 'aaa'), ('#bbb', 'bbb'), ('#ccc', 'ccc'),
              ('#ddd', 'ddd'), ('#eee', 'eee'), ('#fff', 'fff'),
              ('#ggg', 'ggg'), ('#hhh', 'hhh'), ('#iii', 'iii')]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '#']

def main():
    """
    Run the genetic algorithm for evolving Ball_Trap_Brain instances.
    
    Returns:
        Ball_Trap_Brain: The best brain found after evolution.
    """
    # Evolution hyperparameters
    generations = 100000
    population_size = 100

    # Initialize population with random brains
    # Parameters: 10 deflectors, 2 bounce energy, alphabet of 6 characters
    population = [Ball_Trap_Brain(100, 2, alphabet, holes_multiplier=2) for _ in range(population_size)]
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
        new_population = [copy.deepcopy(best_individual).Mutate(0.05) for _ in range(population_size)]
        population = new_population
        print(f"Generation {generation}: Best fitness = {best_fitness}")
    
    return best_individual

# Run the genetic algorithm and store the best evolved brain
brain = main()
while True:
    i = input("Input some text: ")
    print(f"output: {''.join(brain.compute_input(i))}")
