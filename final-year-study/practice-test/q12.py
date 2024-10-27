from numbers import Number

network = {
    
    'A' : {
        'Parents' : ['C'],
        'CPT' : {
            (True,): 0.8, # P(A=True | C=True)
            (False,): 0.2 # P(A=True | C=False)
        }
    },

    'B' : {
        'Parents' : ['A', 'D'],
        'CPT' : {
            (True, True): 0.9, # P(B=True | A=True, D=True)
            (True, False): 0.8, # P(B=True | A=True, D=False)
            (False, True): 0.7, # P(B=True | A=False, D=True)
            (False, False): 0.6, # P(B=True | A=False, D=False)
        }
    },

    'C' : {
        'Parents' : [],
        'CPT' : {
            (): 0.5 # P(C=True)
        }
    },

    'D' : {
        'Parents': [],
        'CPT' : {
            () : 0.5 # P(D=True)
        }
    }
}


#### ENSURE EACH PROBABILITY IS UNIQUE

# test
# Checking the overall type-correctness of the network
# without checking anything question-specific

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")