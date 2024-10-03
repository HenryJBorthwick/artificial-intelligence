def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will eventually hold the value we are interested in

    # for each parent(variable) in network
    for var in network:
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 

        # get assigned value (True/False)
        var_value = assignment[var]

        # get parents of variable
        parents = network[var]['Parents']

        # get values from each of the parents
        parents_values = tuple(assignment[parent] for parent in parents)

        # get CPT (Constraint Probability Table) or probability
        cpt = network[var]['CPT']

        # get prob of var being true given parents values (Correct Probability)
        prob_true = cpt[parents_values]

        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.

        # determine correct probability off var_value
        if var_value:
            prob = prob_true # P(var=True | parents)
        else:
            prob = 1 - prob_true # P(var=False | parents)
        
        # update joint probability
        p *= prob
    
    return p


#tests
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))

print("\n")


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': False})
print("{:.5f}".format(p))

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
 
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p)) 

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
 
p = joint_prob(network, {'A': False, 'B':False})
print("{:.5f}".format(p))
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p))
p = joint_prob(network, {'A': True, 'B':False})
print("{:.5f}".format(p))
p = joint_prob(network, {'A': True, 'B':True})
print("{:.5f}".format(p)) 

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

p = joint_prob(network, {'John': True, 'Mary': True,
                         'Alarm': True, 'Burglary': False,
                         'Earthquake': False})
print("{:.8f}".format(p))  