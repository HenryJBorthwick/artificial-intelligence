from csp import Relation, scope, satisfies, CSP
import itertools

# CSP TO CONVERT
csp = CSP(
    var_domains={var: {0, 1, 2} for var in 'abcd'},
    constraints={
        lambda a, b, c: a > b + c,
        lambda c, d: c > d
    }
)


# RELATION TO CREATE
# relations = [
#     Relation(
#         ### COMPLETE ###
#     ),
#
#     ### COMPLETE ###
# ]

# ANSWER RELATION
relations = [
    Relation(header=['a', 'b', 'c'],
             tuples={(1, 0, 0), (2, 0, 0), (2, 0, 1), (2, 1, 0)}),

    Relation(header=['c', 'd'],
             tuples={(1, 0), (2, 0), (2, 1)})
]

# TEST 1
print(len(relations))
print(all(type(r) is Relation for r in relations))

# TEST 1 EXPECTED RESULT
# 2
# True

# TEST 2
def csp_to_relations(csp):
    relations = []

    for constraint in csp.constraints:
        vars_in_scope = sorted(scope(constraint))  # Get variables in the constraint's scope, sorted alphabetically
        tuples = set()

        # Generate all possible assignments for the variables in the scope
        for values in itertools.product(*(csp.var_domains[var] for var in vars_in_scope)):
            assignment = dict(zip(vars_in_scope, values))
            if satisfies(assignment, constraint):
                tuples.add(values)

        # Create the relation and add to the list of relations
        relations.append(Relation(header=vars_in_scope, tuples=tuples))

    return relations


# Convert the CSP instance to a list of relations
relations = csp_to_relations(csp)

# Output the results for verification
for relation in relations:
    print(f"Relation(header={relation.header},")
    print(f"         tuples={{{', '.join(map(str, sorted(relation.tuples)))}}})")
    print()
