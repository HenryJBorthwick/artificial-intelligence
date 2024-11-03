network = {
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01
        }
    },

    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95, #P(A=True|Virus=True)
            (False,): 0.10 #P(A=True|Virus=False)
        }
    },

    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.90, #P(B=True|Virus=True)
            (False,): 0.05 #P(B=True|Virus=False)
        }
    }
}