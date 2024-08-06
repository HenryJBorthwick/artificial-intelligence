import re
from search import *


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


class KBGraph(Graph):
    def __init__(self, kb, query):
        # Parse knowledge base into list of clauses
        self.clauses = list(clauses(kb))
        # query trying to prove
        self.query = query

    def starting_nodes(self):
        # Initial node of query list
        return [list(self.query)]

    def is_goal(self, node):
        # Goal reached when no more atom to prove
        return len(node) == 0

    def outgoing_arcs(self, tail_node):
        arcs = []

        # For each atom in tail node
        for atom in tail_node:
            # For each clause in knowledge base
            for head, body in self.clauses:
                # Head clause math atom trying to prove
                if head == atom:
                    # Create a new state by removing the proven atom and adding the body atoms
                    new_state = [a for a in tail_node if a != atom] + body
                    arcs.append(Arc(tail_node, new_state, str(atom) + " :- " + ", ".join(body), len(arcs)))
        return arcs


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        self.container = []

    def __iter__(self):
        return self

    def add(self, path):
        self.container.append(path)

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration

def main():
    # Test 1
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
    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    # Test 2
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
    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    # Test 3
    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """
    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    # Test 4
    kb = """
    a :- b.
    """
    query = {'c'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")


if __name__ == "__main__":
    main()
