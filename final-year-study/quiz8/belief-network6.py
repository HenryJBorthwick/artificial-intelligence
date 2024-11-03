network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1 #P(A=True)
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.2, #P(B=True|A=False)
            (True,): 0.3 #P(B=True|A=True)
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.45, #P(C=True|A=False)
            (True,): 0.45 #(C=True|A=True)
            }},
}


print(sorted(network.keys()))