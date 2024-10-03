from itertools import product

def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}

    raw_distribution = {True: 0.0, False: 0.0}

    for query_value in {True, False}:

        assignment = dict(evidence)
        assignment[query_var] = query_value

        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}

            full_assignment = {**assignment, **hidden_assignments}

            prob = join_probability(network, full_assignment)

            raw_distribution[query_value] += prob


    total = raw_distribution[True] + raw_distribution[False]
    normalized_distribution = {
        True: raw_distribution[True] / total,
        False: raw_distribution[False] / total
    }

    return normalized_distribution


def join_probability(network, assignment):

    p = 1.0

    for var in network:

        var_value = assignment[var]

        parents = network[var]['Parents']

        parent_values = tuple(assignment[parent] for parent in parents)

        prob_true = network[var]['CPT'][parent_values]

        if var_value:
            prob = prob_true
        else:
            prob = 1 - prob_true

        p *= prob

    return p    

# tests
network = {
    'Virus': {
        'Parents':[],
        'CPT': {
            (): 0.01
        }
    },
    'A': {
        'Parents':['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.10
        }
    },
    'B': {
        'Parents':['Virus'],
        'CPT': {
            (True,): 0.90,
            (False,):0.05
        }
    }
}

answer = query(network, 'Virus', {'A': True})
print("The probability of carrying the virus\n"
      "if test A is positive: {:.5f}"
      .format(answer[True]))

answer = query(network, 'Virus', {'B': True})
print("The probability of carrying the virus\n"
      "if test B is positive: {:.5f}"
      .format(answer[True]))