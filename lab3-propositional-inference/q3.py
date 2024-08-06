# import any module as necessary
from itertools import *


def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """

    return {atom for atom in formula.__code__.co_varnames}


def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)


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


def models(knowledge_base):
    # Get all atoms in the knowledge base
    all_atoms = set()
    for formula in knowledge_base:
        # Update set to include atoms from each formula
        all_atoms.update(atoms(formula))

    # Generate all the possible permutations
    all_interpretations = interpretations(all_atoms)

    valid_models = []
    for interpretation in all_interpretations:
        if all(value(formula, interpretation) for formula in knowledge_base):
            valid_models.append(interpretation)

    return valid_models


def main():
    # test 1
    knowledge_base = {
        lambda a, b: a and not b,
        lambda c: c
    }

    print(models(knowledge_base))

    # test 2
    knowledge_base = {
        lambda a, b: a and not b,
        lambda c, d: c or d
    }

    for interpretation in models(knowledge_base):
        print(interpretation)


if __name__ == '__main__':
    main()
