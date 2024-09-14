from itertools import product

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


def models(knowledge_base):

    #init a set
    atom_set = set()

    # get set of all atoms
    for proposition in knowledge_base:
        atom_set.update(atoms(proposition))

    # create all interpretations
    all_interpretations = interpretations(atom_set)

    # init list of interpretations that satisfy conditons
    model = list()

    # evaluate each proposition with lambda expressions
    for interpretation in all_interpretations:
        # check that all formulas are evluate to true
        if all(value(formula, interpretation) for formula in knowledge_base):
            model.append(interpretation)

    return model



# test1
knowledge_base = {
    lambda a, b: a and not b,
    lambda c: c
}

print(models(knowledge_base))

# result1
# [{'a': True, 'b': False, 'c': True}]

# test2
knowledge_base = {
    lambda a, b: a and not b,
    lambda c, d: c or d
}

for interpretation in models(knowledge_base):
    print(interpretation)

# result2
# {'a': True, 'b': False, 'c': False, 'd': True}
# {'a': True, 'b': False, 'c': True, 'd': False}
# {'a': True, 'b': False, 'c': True, 'd': True}