# Bouncy_Ball_AI

A small Python project that models a bouncing ball through a set of randomized deflectors and alphabet-based inputs. The `Ball_Trap_Brain` class assigns starting positions, directions, and deflector values, then simulates how input characters travel and ricochet to produce an output sequence.

## Project structure

- `Main.py` - example runner that creates a `Ball_Trap_Brain`, computes output for a sample input, and displays deflector configuration.
- `Ball_Brain.py` - implementation of the `Ball_Trap_Brain` class and the bouncing ball logic.

## Features

- Randomized deflectors and travel paths
- Alphabet-based input mapping to starting positions and directions
- Recursive ball ricochet simulation with energy tracking
- Output collection when a ball lands on a deflector containing a non-integer value

## Requirements

- Python 3

## Usage

Run the main program from the repository root:

```bash
python3 Main.py
```

This will:

1. create a `Ball_Trap_Brain` instance with a fixed number of deflectors, bounce energy, and alphabet
2. compute the output for the sample input string `abcde`
3. print the generated deflector list and the computed output

## Customization

You can change the brain setup by editing `Main.py`:

- first argument: number of deflectors
- second argument: base bounce energy
- third argument: alphabet list

For example:

```python
brain = Ball_Trap_Brain(12, 3, ['a', 'b', 'c', 'd', 'e', 'f'])
```

Then run `python3 Main.py` again.

## Notes

- The simulation uses random values for deflector targets and hole assignments, so output may differ each run.
- The current implementation prints ball energy and position information during ricochet processing.
