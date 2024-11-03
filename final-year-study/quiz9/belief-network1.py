network = {
    'Y': {
        'Parents': [],
        'CPT': { 
            (): (4+2) / (7 + 2 * 2) #P(Y=True)
        }
    },

    'X1': {
        'Parents': ['Y'],
        'CPT': { 
            (True,): (1+2) / (4 + 2 * 2), #P(X1=True|Y=True)
            (False,): (3+2) / (3 + 2 * 2) #P(X1=True|Y=False)
        }
    },

    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (1+2) / (4 + 2 * 2), #P(X2=True|Y=True)
            (False,): (2+2) / (3+2*2) #P(X2=True|Y=False)
        }
    },

    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (0+2)/(4+2*2), #P(X3=True|Y=True)
            (False,): (0+2)/(3+2*2) #P(X3=True|Y=False)
        }
    },
}