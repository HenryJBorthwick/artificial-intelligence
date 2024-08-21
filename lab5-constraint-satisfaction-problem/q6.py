from csp import Relation, scope, satisfies, CSP
import itertools

# CSP TO CONVERT
csp = CSP(
    var_domains={var: {-1, 0, 1} for var in 'abcd'},
    constraints={
        lambda a, b: a == abs(b),
        lambda c, d: c > d,
        lambda a, b, c: a * b > c + 1
    }
)

# TO COMPLETE
# relations = [
#
#     ### COMPLETE ###
#
# ]

# COMPLETED
relations = [
    Relation(header=['a', 'b'],
             tuples={(0, 0),
                     (1, -1),
                     (1, 1)}),

    Relation(header=['c', 'd'],
             tuples={(1, -1),
                     (1, 0),
                     (0, -1)}),

    Relation(header=['a', 'b', 'c'],
             tuples={(1, 1, -1),
                     (-1, -1, -1)})
]

relations_after_elimination = [
    # STAYS SAME AS DOES NOT INVOLVE A
    Relation(header=['c', 'd'],
             tuples={(1, -1),
                     (1, 0),
                     (0, -1)}),

    # JUST COMPUTE RELATION AGAIN WITHOUT A
    Relation(header=['b', 'c'],
             tuples={(1, -1)})
]
