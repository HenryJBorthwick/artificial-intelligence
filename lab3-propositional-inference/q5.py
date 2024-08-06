import re


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(knowledge_base):
    # Parse knowledge bsae into clauses
    clauses_list = list(clauses(knowledge_base))

    # Initialize set of derived atoms
    dervied_atoms = set()

    # Track if new atoms were added in last iteration
    added_new_atom = True

    while added_new_atom:
        # Rest for iteration
        added_new_atom = False

        # Iteration over each clause in knowledge base
        for head, body in clauses_list:
            # Check if atoms in boyd are already derived
            if all(atom in dervied_atoms for atom in body):
                # If head not derived, add it to the derived atoms
                if head not in dervied_atoms:
                    dervied_atoms.add(head)
                    added_new_atom = True

    return dervied_atoms


def main():
    # test 1
    kb = """
    a :- b.
    b.
    """

    print(", ".join(sorted(forward_deduce(kb))))

    # test 2
    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """

    print(", ".join(sorted(forward_deduce(kb))))

    # test 3
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    print(", ".join(sorted(forward_deduce(kb))))

if __name__ == "__main__":
    main()