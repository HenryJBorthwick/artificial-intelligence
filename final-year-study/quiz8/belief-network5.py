network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 # P(A=True)
            }        
    },

    'B': {
        'Parents': [],
        'CPT': {
            (): 0.3 # P(B=True)
        }
    },

    'C': {
        'Parents': [],
        'CPT' : {
            (): 0.7 # P(C=True)
        }
    },

    'D' : {
        'Parents': ['B'],
        'CPT' : {
            (True,): 0.1, #P(D=True|B=True)
            (False,): 0.9 #P(D=True|B=False)
        }
    },

    'E' : {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.1, #P(E=True|B=True)
            (False,): 0.7 #P(E=True|B=False)
        },
    }
}