import itertools
from csp import CSP, satisfies, scope


def gac(csp):
    """
    General Arc Consistency algorithm implementation for CSPs.

    Parameters:
    csp (CSP): An instance of the CSP class representing the problem.

    Returns:
    dict: A dictionary with variables as keys and their pruned domains as values.
    """
    var_domains = {var: set(domain) for var, domain in csp.var_domains.items()}
    to_do = {(X, c) for c in csp.constraints for X in scope(c) if X in csp.var_domains}

    while to_do:
        X, c = to_do.pop()
        Y_vars = scope(c) - {X}
        ND_X = set()

        for x in var_domains[X]:
            assignment = {X: x}
            if any(satisfies(assignment | dict(zip(Y_vars, values)), c) for values in
                   itertools.product(*(var_domains[Y] for Y in Y_vars))):
                ND_X.add(x)

        if ND_X != var_domains[X]:
            var_domains[X] = ND_X
            if not ND_X:
                return None
            to_do |= {(Z, c_prime) for c_prime in csp.constraints
                      for Z in scope(c_prime) if X in scope(c_prime) and Z != X}

    return var_domains


# TEST 1
canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })


# Running GAC on the test case
pruned_domains = gac(canterbury_colouring)

# Display the pruned domains
if pruned_domains:
    for var, domain in pruned_domains.items():
        print(f"{var}: {sorted(domain)}")
else:
    print("No solution exists.")
