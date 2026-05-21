import difflib
from Ball_Brain import Ball_Trap_Brain
import math

def evaluate_performance(input_val, answer, brain):
    output = brain.compute_input(input_val)
    return difflib.SequenceMatcher(None, output, answer).ratio()

def evaluate_population(population, test_cases):
    results = []
    for individual in population:
        individual_results = []
        for input_val, answer in test_cases:
            individual_results.append(evaluate_performance(input_val, answer, individual))
        results.append(sum(individual_results) / len(individual_results))
    idx = results.index(max(results))
    return max(results), population[idx]
