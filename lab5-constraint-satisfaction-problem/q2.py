from csp import CSP
from q1 import generate_and_test


crossword_puzzle = CSP(
    # GOAL IS TO ADJUST THE DOMAIN TO PASS ALL TESTS
    # ORIGINAL
    # var_domains={
    #     # read across:
    #     'across1': set("ant big bus car has".split()),
    #     'across3': set("book buys hold lane year".split()),
    #     'across4': set("ant big bus car has".split()),
    #     # read down:
    #     'down1': set("book buys hold lane year".split()),
    #     'down2': set("ginger search symbol syntax".split()),
    #     },

    # AFTER SOLVING BY HAND
    var_domains={
        # read across:
        'across1': set("bus has".split()),
        'across3': set("lane year".split()),
        'across4': set("ant car".split()),
        # read down:
        'down1': set("buys hold".split()),
        'down2': set("search syntax".split()),
    },

    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
        })


# CHEAT SOLUTION CODE
# solutions = sorted(str(sorted(solution.items())) for solution
#                    in generate_and_test(crossword_puzzle))
# print("\n".join(solutions))

# TEST 1
print(sorted(crossword_puzzle.var_domains['across1']))

# TEST 2
print(sorted(crossword_puzzle.var_domains['across3']))

# TEST 3
print(sorted(crossword_puzzle.var_domains['across4']))

# TEST 4
print(sorted(crossword_puzzle.var_domains['down1']))

# TEST 5
print(sorted(crossword_puzzle.var_domains['down2']))