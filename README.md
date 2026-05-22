# Bouncy_Ball_AI

A Python project that evolves a simple bouncing-ball brain using a genetic algorithm. The brain is represented by a network of randomized deflectors, and the system learns to convert input strings into target output strings by evolving the deflector configuration.

## Repository files

- `Main.py` - runs the genetic algorithm, evaluates a population, and evolves the best performing brain.
- `Ball_Brain.py` - defines the `Ball_Trap_Brain` class, including ball travel, ricochet behavior, and mutation.
- `Evaluation.py` - evaluates brain output fitness using string similarity over a set of test cases.

## How it works

1. `Main.py` builds a population of `Ball_Trap_Brain` instances.
2. Each brain maps input characters to start positions and movement directions.
3. The brain simulates ball travel through deflectors.
4. When a ball lands on a deflector containing a character, that character is added to the output.
5. `Evaluation.py` scores outputs against expected results using `difflib.SequenceMatcher`.
6. The best brain is mutated to form the next generation.

## Requirements

- Python 3.x

## Usage

From the repository root, run:

```bash
python3 Main.py
```

The script will evolve a population of brains and print the best fitness each generation. Once the evolutionary loop completes, it enters an interactive prompt where you can type input text and see the brain's computed output.

## Configuration

In `Main.py`, key parameters include:

```python
generations = 100000
population_size = 100
```

`Ball_Trap_Brain` is instantiated as:

```python
Ball_Trap_Brain(100, 2, alphabet, holes_multiplier=2)
```

- `100` = number of deflectors
- `2` = base bounce energy
- `alphabet` = list of supported input/output characters
- `holes_multiplier` = number of character-containing deflectors relative to alphabet size

## Test cases

The current `test_cases` in `Main.py` include combinations such as:

- `#a` → `a`
- `#b` → `b`
- `#abc` → `abc`
- `#def` → `def`
- `#ghi` → `ghi`

These are used to measure how closely the brain's output matches expected strings.

## Notes

- The algorithm is stochastic, so results vary between runs.
- Evolution may take many generations to improve fitness, especially with a large alphabet.
- `Ball_Trap_Brain.compute_input()` returns a list of output characters; `Main.py` joins that list before printing.
- The interactive prompt continues until interrupted with `Ctrl+C`.
