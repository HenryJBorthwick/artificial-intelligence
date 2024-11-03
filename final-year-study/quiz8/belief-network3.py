network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001 #P(Disease=True)
        }
    },

    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99, #P(Test=True|Disease=True)
            (False,): 0.01 #P(Test=True|Disease=False)
        }
    }
}