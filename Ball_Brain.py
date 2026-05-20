import random

class Ball_Trap_Brain:
    def __init__(self, deflectors, bounce, alphabet):
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
        output = []

        for i in input:
            if i in self.alphabet:
                index = self.alphabet.index(i)
                directions.append(self.alphabet_directions[index])
                positions.append(self.alphabet_start_positions[index])

        for i in range(len(directions)):
            travel.append(self.travel(directions, positions[i], i))

        for i in range(len(travel)):
            if not isinstance(self.deflectors_list[travel[i]][1], int):
                output.append(self.deflectors_list[travel[i]][1])

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

    

    