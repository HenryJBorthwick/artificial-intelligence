from itertools import *


def interpretations(atoms):
    # List of sorted atoms to ensure alphabetical order. Columns of truth table.
    sorted_atoms = sorted(atoms, key=lambda atom: atom)

    # List of all combinations true values from the given atoms. Rows of truth table.
    truth_values = product([False, True], repeat=len(atoms))

    # Truth table as list of dicts
    truth_table_dict_list = []

    # Iterate for each row in truth table
    for values in truth_values:
        # Fill dict row by row
        truth_table_dict = {}
        for atom, value in zip(sorted_atoms, values):
            truth_table_dict[atom] = value

        # Add row to list of dicts
        truth_table_dict_list.append(truth_table_dict)

    return truth_table_dict_list


def main():
    # test 1
    atoms = {'q', 'p'}
    for i in interpretations(atoms):
        print(i)

    # test 2
    atoms = {'human', 'mortal', 'rational'}
    for i in interpretations(atoms):
        print(i)


if __name__ == '__main__':
    main()
