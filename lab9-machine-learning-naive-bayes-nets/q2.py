def posterior(prior, likelihood, observation):
    # Initialize the numerators with the prior probabilities
    numerator_true = prior            # P(Class=True)
    numerator_false = 1 - prior       # P(Class=False)

    # Update the numerators by multiplying with the likelihoods for each feature
    for i in range(len(observation)):
        # Observed value for feature X[i]
        obs = observation[i]

        # Retrieve the likelihoods for the current feature
        # P(X[i]=True | Class=True)
        p_xi_given_C_true = likelihood[i][True]
        # P(X[i]=True | Class=False)
        p_xi_given_C_false = likelihood[i][False]

        # Adjust the likelihoods based on the observed value
        # If the observed value is False, use P(X[i]=False | Class)
        if not obs:
            # P(X[i]=False | Class) = 1 - P(X[i]=True | Class)
            p_xi_given_C_true = 1 - p_xi_given_C_true
            p_xi_given_C_false = 1 - p_xi_given_C_false

        # Multiply the likelihoods into the numerators
        numerator_true *= p_xi_given_C_true
        numerator_false *= p_xi_given_C_false

    # Compute the denominator, which is the total probability of the observation
    # sum the two numerators
    denominator = numerator_true + numerator_false

    # Compute the posterior probability by normalizing the numerator for Class=True
    # P(Class=True | observation)
    posterior_true = numerator_true / denominator  

    # Return the posterior probability
    return posterior_true



#tests
prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  

print('\n')

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  

print('\n')

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (False, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  

print('\n')


prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (False, False, False)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  