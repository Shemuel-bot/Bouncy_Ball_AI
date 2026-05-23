"""
Fitness evaluation module for Ball_Trap_Brain genetic algorithm.

This module contains functions to evaluate the performance of individual brains
and entire populations against test cases using string similarity metrics.
"""

import difflib
from Ball_Brain import Ball_Trap_Brain
import math


def evaluate_performance(input_val, answer, brain):
    """
    Evaluate how well a brain performs on a single test case.
    
    Uses SequenceMatcher to compute string similarity between the brain's output
    and the expected answer, returning a fitness score between 0 and 1.
    
    Args:
        input_val (str): Input string to feed to the brain.
        answer (str): Expected output string.
        brain (Ball_Trap_Brain): The brain to evaluate.
    
    Returns:
        float: Fitness score (0 to 1) where 1.0 is a perfect match.
    """
    output = brain.compute_input(input_val)
    return 1 if ''.join(output) == answer else 0


def evaluate_population(population, test_cases):
    """
    Evaluate an entire population against all test cases.
    
    Computes the average fitness for each brain across all test cases, then
    returns the best-performing brain and its overall fitness score.
    
    Args:
        population (list): List of Ball_Trap_Brain instances to evaluate.
        test_cases (list): List of tuples (input_string, expected_output_string).
    
    Returns:
        tuple: (best_fitness, best_brain) where best_fitness is between 0 and 1.
    """
    # Evaluate each brain on all test cases
    results = []
    for individual in population:
        individual_results = []
        # Calculate fitness for this brain on each test case
        for input_val, answer in test_cases:
            individual_results.append(evaluate_performance(input_val, answer, individual))
        # Average fitness across all test cases for this brain
        results.append(sum(individual_results) / len(individual_results))
    
    # Find the brain with the highest fitness
    idx = results.index(max(results))
    return max(results), population[idx]
