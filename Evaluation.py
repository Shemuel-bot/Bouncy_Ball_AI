import difflib

def evaluate_performance(expected, actual):
    return difflib.SequenceMatcher(None, expected, actual).ratio()

def evaluate_population(population, expected):
    results = []
    for individual in population:
        results.append(evaluate_performance(expected, individual))
    idx = results.index(max(results))
    return max(results), population[idx]
