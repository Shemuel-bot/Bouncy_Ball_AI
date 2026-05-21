import random
import math

class Ball_Trap_Brain:
    def __init__(self, deflectors, bounce, alphabet):
        self.ball_energy = bounce*2
        self.alphabet = alphabet
        self.alphabet_directions = self.choose_alphabet_direction(len(alphabet))
        self.alphabet_start_positions = self.start_positions(len(alphabet), deflectors)
        self.deflectors_list = [[random.randint(0, deflectors-1), bounce] for i in range(deflectors)]
        self.set_holes(alphabet, deflectors)

    def set_holes (self, alphabet, deflectors):
        holes = len(alphabet)
        for i in range(holes):
            self.deflectors_list[random.randint(0, deflectors-1)][1] = random.choice(alphabet)

    def choose_alphabet_direction(self, alphabet):
        directions = []
        for i in range(alphabet):
            if random.choice([True, False]):
                directions.append('left')
                continue
            directions.append('right')
        return directions
    
    def start_positions(self, alphabet, deflectors):
        positions = []
        for i in range(alphabet):
            position = random.randint(0, deflectors-1)
            positions.append(position)
        return positions

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
            travel.append(self.travel(directions, positions[i], i))


        return self.ricochet(travel, 10, self.ball_energy)
        
    def ricochet(self, travel, cap, ball_energy):
        output = []
        for i in range(len(travel)):
            new_idx = travel[i] if abs(travel[i]) < len(self.deflectors_list) else abs(travel[i]) % len(self.deflectors_list)
            i = 0
            while self.ball_energy > 0 and i < cap:
                distance = abs(self.deflectors_list[new_idx][0] - new_idx)
                
                if not isinstance(self.deflectors_list[new_idx][1], int):
                    output.append(self.deflectors_list[new_idx][1])
                    self.ball_energy += 1
                    self.ball_energy -= distance
                    new_idx = self.deflectors_list[new_idx][0]
                    i += 1
                    continue

                self.ball_energy += self.deflectors_list[new_idx][1]
                self.ball_energy -= distance

                new_idx = self.deflectors_list[new_idx][0]
                i += 1
            self.ball_energy = ball_energy
        return output


    def travel(self, directions, position, index):
        for i in range(len(directions)):
            if i == index:
                continue
            if directions[i] == 'left':
                position -= 1
            else:
                position += 1
        return position

    def display_deflectors(self):
        for i, deflect in enumerate(self.deflectors_list):
            print(f"Deflector {i}: {deflect}")

    def Mutate(self, probability=0.1):
        if random.random() < probability:
            for i in range(len(self.deflectors_list)):
                if random.random() < probability:
                    self.deflectors_list[i] = [random.randint(0, len(self.deflectors_list)-1), random.choice(self.alphabet)]
            
            for i in range(len(self.alphabet_directions)):
                if random.random() < probability:
                    self.alphabet_directions[i] = random.choice(['left', 'right'])

            for i in range(len(self.alphabet_start_positions)):
                if random.random() < probability:
                    self.alphabet_start_positions[i] = random.randint(0, len(self.deflectors_list)-1)