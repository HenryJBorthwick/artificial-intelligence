from itertools import product

def interpretations(atoms):

    # Create Values
    values = {True, False}

    # Generate Cartesian Product For All Possible Assignment
    combinations = list(product(values, repeat=len(atoms)))

    # init truth table
    interpretations = []

    # Sort Atoms Alphabetically
    atoms = sorted(list(atoms))

    # init dict
    for combination in combinations:

        # assign each atom the possible truth values
        interpretation = zip(atoms, combination)

        # convert to dict
        interpretation = dict(interpretation)

        # add row to truth table
        interpretations.append(interpretation)
    
    return interpretations


#test1
atoms = {'q', 'p'}
for i in interpretations(atoms):
    print(i)

#expected result1
# {'p': False, 'q': False}
# {'p': False, 'q': True}
# {'p': True, 'q': False}
# {'p': True, 'q': True}


#test2
atoms = {'human', 'mortal', 'rational'}
for i in interpretations(atoms):
    print(i)

# expected result2
# {'human': False, 'mortal': False, 'rational': False}
# {'human': False, 'mortal': False, 'rational': True}
# {'human': False, 'mortal': True, 'rational': False}
# {'human': False, 'mortal': True, 'rational': True}
# {'human': True, 'mortal': False, 'rational': False}
# {'human': True, 'mortal': False, 'rational': True}
# {'human': True, 'mortal': True, 'rational': False}
# {'human': True, 'mortal': True, 'rational': True}