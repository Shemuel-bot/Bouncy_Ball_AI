import random
import math
import copy

class Ball_Trap_Brain:
    def __init__(self, deflectors, bounce, alphabet, holes_multiplier=1):
        self.holes_multiplier = holes_multiplier
        self.ball_energy = bounce*2
        self.alphabet = alphabet
        self.alphabet_directions = self.choose_alphabet_direction(len(alphabet))
        self.alphabet_start_positions = self.start_positions(len(alphabet), deflectors)
        self.deflectors_list = [[random.randint(0, deflectors-1), bounce] for i in range(deflectors)]
        self.set_holes(alphabet, deflectors, self.holes_multiplier)

    def set_holes (self, alphabet, deflectors, holes_multiplier):
        holes = len(alphabet) * holes_multiplier
        for i in range(holes):
            self.deflectors_list[random.randint(0, deflectors-1)][1] = random.choice(alphabet)

    def choose_alphabet_direction(self, alphabet):
        directions = [random.choice([1,-1]) for _ in range(alphabet)]
        return directions
    
    def start_positions(self, alphabet, deflectors):
        return [random.randint(0, deflectors-1) for i in range(alphabet)]
       

    def compute_input(self, input):
        directions = []
        positions = []
        travel = []

        for i in input:
            if i in self.alphabet:
                index = self.alphabet.index(i)
                directions.append(self.alphabet_directions[index])
                positions.append(self.alphabet_start_positions[index])

        for i in range(len(directions)):
            travel.append(self.travel(copy.copy(directions), positions[i], i))


        return self.ricochet(travel, 10, self.ball_energy)
        
    def ricochet(self, travel, cap, ball_energy):
        output = []
        dl = self.deflectors_list
        n = len(dl)

        for t in travel:
            # normalize index using modulo (handles large or negative values)
            new_idx = t % n
            cap_idx = 0
            be = ball_energy

            while be > 0 and cap_idx < cap:
                dest, val = dl[new_idx]
                distance = abs(dest - new_idx)

                if not isinstance(val, int):
                    output.append(val)
                    be += 1
                    be -= distance
                    new_idx = dest
                    cap_idx += 1
                    continue

                be += val
                be -= distance
                new_idx = dest
                cap_idx += 1

        return output


    def travel(self, directions, position, index):
        directions.pop(index)
        position += sum(directions)
        return position

    def display_deflectors(self):
        for i, deflect in enumerate(self.deflectors_list):
            print(f"Deflector {i}: {deflect}")

    def Mutate(self, individual_probability=0.1, probability=0.05):
        if random.random() < individual_probability:
            for i in range(len(self.deflectors_list)):
                if random.random() < probability:
                    self.deflectors_list[i][0] = random.randint(0, len(self.deflectors_list)-1)

            for i in range(len(self.deflectors_list)):
                if random.random() < probability:
                    self.deflectors_list[random.randint(0, len(self.deflectors_list)-1)][1] = random.choice(self.alphabet)
            
            for i in range(len(self.alphabet_directions)):
                if random.random() < probability:
                    self.alphabet_directions[i] = random.choice([1, -1])

            for i in range(len(self.alphabet_start_positions)):
                if random.random() < probability:
                    self.alphabet_start_positions[i] = random.randint(0, len(self.deflectors_list)-1)
                    
            if random.random() < probability:
                self.set_holes(self.alphabet, len(self.deflectors_list), self.holes_multiplier)

        return self