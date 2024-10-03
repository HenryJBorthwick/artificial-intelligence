from itertools import product

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}

    # Initialise a raw distribution to [0, 0]
    raw_distribution = {True: 0.0, False: 0.0}

    # Iterate over possible values of query variable (True or False)
    for query_value in {True, False}:

        # Create full assignment starting with evidence and query_var
        assignment = dict(evidence) # create a partial assignment (Copy Evidence)
        assignment[query_var] = query_value #(Set query values)

        # Update the assignment to include the query variable (Enumerate all possible assignments of hidden variables)
        for values in product((True, False), repeat=len(hidden_vars)):
            # Update the assignment (we now have a complete assignment)
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)} # Provided code
            # OR
            # hidden_assignments = dict(zip(hidden_assignments, values)) # Simpler version

            # Merge Dictionaries
            full_assignment = {**assignment, **hidden_assignments}

            # compute join probability
            prob = join_probability(network, full_assignment)
            
            # Update the raw distribution by the probability of the assignment.
            raw_distribution[query_value] += prob

    # Normalise the raw distribution and return it
    total = raw_distribution[True] + raw_distribution[False]
    normalized_distribution = {
        True: raw_distribution[True] / total,
        False: raw_distribution[False] / total
    }

    return normalized_distribution


def join_probability(network, assignment):

    p = 1.0

    for var in network:

        # get var value
        var_value = assignment[var]

        # get var parents
        parents = network[var]['Parents']

        # get parent values
        parent_values = tuple(assignment[parent] for parent in parents)

        # get prob values
        prob_true = network[var]['CPT'][parent_values]

        if var_value:
            prob = prob_true
        else:
            prob = 1 - prob_true

        p *= prob

    return p    


# tests
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))

print("\n")

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))

print("\n")

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {})
print("P(B=true) = {:.5f}".format(answer[True]))
print("P(B=false) = {:.5f}".format(answer[False]))

print("\n")

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True])) 

print("\n")

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'John', {'Mary': True})
print("Probability of John calling if\n"
      "Mary has called: {:.5f}".format(answer[True])) 