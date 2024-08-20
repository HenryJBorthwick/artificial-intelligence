from csp import CSP, scope, satisfies
import itertools  # Import itertools for generating Cartesian products


def GAC(csp):
    # Initialize the domains (Dx) for each variable
    var_domains = {var: set(domain) for var, domain in csp.var_domains.items()}

    # Initialize the to_do set with all arcs (X, c) where X is in the scope of c
    to_do = {(X, c) for c in csp.constraints for X in scope(c)}

    # While there are arcs to process
    while to_do:
        # Select and remove an arc (X, c) from to_do
        X, c = to_do.pop()

        # Scope of the constraint
        scp = scope(c)

        # Compute the new domain for X (NDX)
        NDX = set()
        for x in var_domains[X]:
            assignment = {X: x}
            if any(satisfies({**assignment, **values}, c) for values in product_domains(var_domains, scp, X)):
                NDX.add(x)

        # If the domain of X has changed
        if NDX != var_domains[X]:
            var_domains[X] = NDX

            # Add to the to_do list any arc (Z, c') where X is in the scope of c'
            # and Z is in the scope of c' but not X
            for c_prime in csp.constraints:
                if X in scope(c_prime):
                    for Z in scope(c_prime):
                        if Z != X:
                            to_do.add((Z, c_prime))

    # Return the pruned domains
    return var_domains


def product_domains(var_domains, scp, exclude_var):
    # Generates combinations of values from the domains of variables in scp excluding exclude_var
    keys = [var for var in scp if var != exclude_var]
    if not keys:
        return [{}]  # Return a list with an empty dict if no variables left
    values_list = [var_domains[var] for var in keys]
    for values in itertools.product(*values_list):
        yield dict(zip(keys, values))


# Define the crossword puzzle CSP as given in your example
crossword_puzzle = CSP(
    var_domains={
        'across1': set("ant big bus car has".split()),
        'across3': set("book buys hold lane year".split()),
        'across4': set("ant big bus car has".split()),
        'down1': set("book buys hold lane year".split()),
        'down2': set("ginger search symbol syntax".split()),
    },
    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
    })

# Apply the GAC algorithm
pruned_domains = GAC(crossword_puzzle)

# Print the pruned domains
for var, domain in pruned_domains.items():
    print(f"{var}: {sorted(domain)}")
