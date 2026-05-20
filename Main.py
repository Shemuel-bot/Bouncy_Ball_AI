from Ball_Brain import Ball_Trap_Brain

# Create an instance of the Ball_Trap_Brain
brain = Ball_Trap_Brain(10, 2, ['a', 'b', 'c', 'd', 'e'])
print(brain.compute_input('abcde'))
brain.display_deflectors()