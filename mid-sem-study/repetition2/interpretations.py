from itertools import product

def interpretations(atoms):
    truth_values = [False, True]

    assignments = list(product(truth_values, repeat=len(atoms)))

    truth_table = []

    atoms = sorted(atoms)

    for assignment in assignments:
        # pq + (True, False)
        row = zip(atoms, assignment)

        # converts iterable zip object into dict
        row = dict(row)
        truth_table.append(row)

    return truth_table



atoms = {'human', 'mortal', 'rational'}
for i in interpretations(atoms):
    print(i)