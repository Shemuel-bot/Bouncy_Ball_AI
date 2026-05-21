# Bouncy_Ball_AI

A Python project that uses evolutionary algorithms to evolve a bouncing ball neural network (`Ball_Trap_Brain`) to produce desired outputs from given inputs. The system simulates a ball ricocheting through randomized deflectors, using genetic mutation to improve brain configurations across generations.

## Project structure

- `Main.py` - genetic algorithm runner that evolves a population of `Ball_Trap_Brain` instances over multiple generations.
- `Ball_Brain.py` - implementation of the `Ball_Trap_Brain` class and the bouncing ball logic.
- `Evaluation.py` - fitness evaluation system that tests evolved brains against test cases.

## Features

- **Genetic Algorithm**: Evolves a population of brains over multiple generations
- **Fitness Evaluation**: Compares brain outputs against expected test cases using string similarity metrics
- **Mutation Mechanism**: Random mutations applied to brain configurations during reproduction
- **Ball Physics**: Randomized deflectors and travel paths with alphabet-based input mapping
- **Recursive Ricochet**: Ball bouncing simulation with energy tracking
- **Character Output**: Output collection when a ball lands on a deflector containing a character value

## Requirements

- Python 3

## Usage

Run the evolutionary algorithm from the repository root:

```bash
python3 Main.py
```

This will:

1. Initialize a population of 100 randomized `Ball_Trap_Brain` instances
2. Run for up to 100 generations, evaluating fitness on predefined test cases
3. Apply mutations to create offspring from the best-performing brain each generation
4. Stop early if a perfect solution (fitness = 1.0) is found

## Test Cases

The algorithm evolves brains to pass the following test cases (input → expected output):

- `'abc'` → `'def'`
- `'bca'` → `'bca'`
- `'cab'` → `'cab'`

Fitness is measured using string similarity between the brain's output and expected output.

## Customization

You can modify the evolution parameters in `Main.py`:

```python
generations = 100          # Number of generations to evolve
population_size = 100      # Number of brains per generation
```

And adjust the brain configuration:

```python
Ball_Trap_Brain(10, 2, ['a', 'b', 'c', 'd', 'e', 'f'])
# Arguments: deflectors, bounce energy, alphabet
```

Modify `test_cases` in `Main.py` to evolve for different input/output mappings.

## How It Works

1. **Initialization**: Each brain has randomized deflectors, starting positions, and directions for each alphabet character
2. **Input Processing**: Input characters are mapped to starting positions and directions
3. **Ball Ricochet**: A ball travels through the deflector maze, bouncing until its energy depletes
4. **Output Generation**: Characters encountered on deflectors with character values are collected as output
5. **Evaluation**: Output is compared to expected results using string similarity (SequenceMatcher ratio)
6. **Evolution**: The best-performing brain is mutated to create the next generation

## Notes

- Output may vary between runs due to random initialization and mutations
- The system continues evolving until either a perfect solution is found or max generations is reached
- Mutation randomly changes deflector configurations of the best brain to explore the solution space
