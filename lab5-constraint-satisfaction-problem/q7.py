from csp import *
import itertools
import copy


def arc_consistent(csp):
    # SUDO CODE
    # for each variable X:
    #     D_X := dom(X)
    #     to_do := {(X, c) | c ∈ C and X ∈ scope(c)}
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)}  # COMPLETE

    # SUDO CODE
    # while to_do is not empty:
    #     select and remove path ⟨X, c⟩ from to_do
    while to_do:
        x, c = to_do.pop()

        # SUDO CODE
        # suppose scope of c is {X, Y1, ..., Yk}
        # NDX := {x | ∈ DX and
        #   exists y1 ∈ DY1, ..., yk ∈ DYk
        #   s.th.c(X=x, Y1=y1, ..., Yk=yk) = true}
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]:  # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):  # COMPLETE
                    new_domain.add(xval)  # COMPLETE
                    break

        # SUDO CODE
        # if NDX ≠ DX:
        #     to_do := to_do ∪ {(Z, c') | X ∈ scope(c'),
        #                       c' is not c, Z ∈ scope(c') \ {X}}
        #     DX := NDX
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime):  # COMPLETE
                        if x != c:  # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain  # COMPLETE

    # SUDO CODE
    # return {DX | X is a variable}
    return csp


def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        # DICT comprehension
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraints) for constraints in csp.constraints):
            yield assignment


# QUESTION 7 STARTS HERE
domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        # UNITS COLUMN CONSTRAINT
        lambda o, r, c1    :      o + o == r + 10 * c1, # one of the constraints
        # add more constraints
        # TENS COLUMN CONSTRAINT
        lambda w, u, c1, c2: w + w + c1 == u + 10 * c2,
        # HUNDREDS COLUMN CONSTRAINT
        lambda t, o, c2, f: t + t + c2 == o + 10 * f,
        # DISTINCT DIGITS CONSTRAINT
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == 6,
        # LEADING DIGIT CONSTRAINT
        lambda t: t != 0,  # t cannot be zero
        # LEADING DIGIT CONSTRAINT
        lambda f: f != 0  # f cannot be zero
        })

# TEST 1
print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twofur"))

# TEST 1 RESULTS
# True
# True


# TEST 2
new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['r']))

# TEST 2 RESULTS
# [0, 2, 4, 6, 8]

# TEST 3
new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))

# TEST 3 RESULTS
# [0, 2, 3, 4, 5, 6, 7, 8, 9]

# TEST 4
new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])

# TEST 4 RESULTS
# 7
# [('f', 1), ('o', 4), ('r', 8), ('t', 7), ('u', 6), ('w', 3)]
# [('f', 1), ('o', 8), ('r', 6), ('t', 9), ('u', 5), ('w', 2)]