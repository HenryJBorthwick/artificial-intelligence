import itertools, copy
from csp import *


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

# TEST 1
simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

csp = arc_consistent(simple_csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))

# TEST 2
csp = CSP(var_domains={x:set(range(10)) for x in 'abc'},
          constraints={lambda a,b,c: 2*a+b+2*c==10})

csp = arc_consistent(csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))
