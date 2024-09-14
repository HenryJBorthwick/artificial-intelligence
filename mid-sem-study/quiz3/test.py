from itertools import product


atoms = {'q', 'p'}

# Create Values List
values = {True, False}

# Generate Cartesian Product, Tuples of truth table values
combinations = list(product(values, repeat=len(atoms)))

print(combinations)

# init truth table
interpretations = []

# init dict
for combination in combinations:
        pairs = zip(atoms, combination)
        
        interpretation = dict(pairs)

        interpretations.append(interpretation)

# print(interpretations)