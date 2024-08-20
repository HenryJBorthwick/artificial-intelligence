from csp import CSP
from q1 import generate_and_test


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

solutions = sorted(str(sorted(solution.items())) for solution
                   in generate_and_test(canterbury_colouring))
print("\n".join(solutions))

# TEST 1
print(sorted(canterbury_colouring.var_domains['christchurch']))

# TEST 2
print(sorted(canterbury_colouring.var_domains['selwyn']))

# TEST 3
print(sorted(canterbury_colouring.var_domains['waimakariri']))