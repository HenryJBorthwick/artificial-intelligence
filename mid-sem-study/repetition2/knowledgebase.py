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

def models(knowledge_base):
    models = []
    atom_set = set()

    for conditional_statement in knowledge_base:
        atom_set.update(atoms(conditional_statement))

    truthtable = interpretations(atom_set)

    for row in truthtable:
        if all(value(formula, row) for formula in knowledge_base):
            models.append(row)

    return models


    
knowledge_base = {
    lambda a, b: a and not b,
    lambda c, d: c or d
}

for interpretation in models(knowledge_base):
    print(interpretation)