network = {
    'Y' : {
        'Parents' : [],
        'CPT' : {
            ():  (4+2) / (7+2+2) #P(Y=True)
        }
    },

    'X1' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (0+2) / (4+2+2), #P(X1=True | Y=True)
            (False,): (1+2) / (3+2+2) #(X1=True | Y=False)
        }
    },


    'X2' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (1+2) / (4+2+2), #P(X2=True | Y=True)
            (False,): (1+2) / (3+2+2) #p(X2=True | Y=False)
        }
    },
}

# only difference is the number of occurrences of condition
# and number of Y for the conditional ones
# p = (Count + k) / (N + k + m)
# count = number of condition
# k = sudocount
# N = number of parent condition
# m = number of states