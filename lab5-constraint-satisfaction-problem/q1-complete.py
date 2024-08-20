import itertools

from csp import *
from itertools import product


def generate_and_test(csp):
    # Get the variables
    variables = csp.var_domains.keys()

    # Get the domains
    domains = csp.var_domains.values()

    # Get the constraints
    constraints = csp.constraints

    # Loop through and Generate all possible solutions from domains
    for poss_val in product(*domains):
        # Map solution values (1,1,1) to variables (a,b,c)
        # Need to put this into dict for satisfies function
        assignment = dict(zip(variables, poss_val))

        results = []
        # Test each possible assignment against each constraint
        for constraint in constraints:
            satisfied = satisfies(assignment, constraint)
            results.append(satisfied)

        # Now check if every element in the results list is true
        all_satisfied = True
        for result in results:
            if result == False:
                all_satisfied = False
                break

        # Return the iterable
        if all_satisfied == True:
            yield assignment

        # NOTE CAN BE CONDENSED USING all()
        # if all(satisfies(assignment, constraint) for constraint in constraints):
        #     yield assignment

# TEST 1
simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
    })

solutions = sorted(str(sorted(solution.items())) for solution
                   in generate_and_test(simple_csp))
print("\n".join(solutions))

# TEST 2
crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("ant,big,bus,car".split(',')),
        'a3': set("book,buys,hold,lane,year".split(',')),
        'a4': set("ant,big,bus,car,has".split(',')),
        # read down:
        'd1': set("book,buys,hold,lane,year".split(',')),
        'd2': set("ginger,search,symbol,syntax".split(',')),
    },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
    })

solution = next(iter(generate_and_test(crossword_puzzle)))

# printing the puzzle similar to the way it actually  looks
pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
    solution['d1'], "", solution['d2'], fillvalue=" ")]
pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
print("\n".join(pretty_puzzle))
