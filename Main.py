from Ball_Brain import Ball_Trap_Brain
import Evaluation
import copy


test_cases = [('abc', 'abc')]


def main():
    generations = 100
    population_size = 10

    population = [Ball_Trap_Brain(10, 2, ['a', 'b', 'c', 'd', 'e']) for _ in range(population_size)]

    for generation in range(generations):
        
        best_fitness, best_individual = Evaluation.evaluate_population(population, test_cases)

        if best_fitness == 1.0:
            print(f"Generation {generation}: Solution found!")
            break

        new_population = [copy.deepcopy(best_individual).Mutate() for _ in range(population_size)]
        population = new_population
        print(f"Generation {generation}: Best fitness = {best_fitness}")
    
main()