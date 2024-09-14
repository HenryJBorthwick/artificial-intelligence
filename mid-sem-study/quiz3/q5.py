import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(kb):

    true_atoms = set()
    rules = []
    
    # Parse the knowledge base
    for head, body in clauses(kb):
        if not body:
            true_atoms.add(head)
        else:
            rules.append((head, body))
    
    # Initialize a flag to track if new atoms are derived
    changed = True
    
    while changed:
        changed = False
        for head, body in rules:
            # Check if all atoms in the body are in true_atoms
            if all(atom in true_atoms for atom in body):
                if head not in true_atoms:
                    true_atoms.add(head)
                    changed = True  # A new atom was added
    return true_atoms

# test 1
kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))

# result 1
# a, b

# print(list(clauses(kb)))

# test 2
kb = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

# result 2
# 

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

# result 3
# a, b, c, d, e