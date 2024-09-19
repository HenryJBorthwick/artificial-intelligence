from itertools import product

def interpretations(atoms):

    truth_values = [False, True]
    assignments = product(truth_values, repeat=len(atoms))

    truth_table = []
    atoms = sorted(atoms)
    for assignment in assignments:
        row = zip(atoms, assignment)
        row = dict(row)
        truth_table.append(row)

    return truth_table


atoms = {'human', 'mortal', 'rational'}
for i in interpretations(atoms):
    print(i)
