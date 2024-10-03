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


#tests q3

# q3 theory answer
network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001 #P(Disease = True) #NOTE: () as no parents
        }
    },
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99, # P(Test=True | Disease=True) #NOTE: () is parent value
            (False,): 0.01 # P(Test=True | Disease=False)
        }
    }
}

answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))

answer = query(network, 'Disease', {'Test': False})
print("The probability of having the disease\n"
      "if the test comes back negative: {:.8f}"
      .format(answer[True]))