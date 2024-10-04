import csv

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    header = training_examples[0]
    data = training_examples[1:]

    total_emails = len(data)
    spam_count = 0
    
    for row in data:
        label = row[-1]
        if label == '1':
            spam_count += 1

    num_classes = 2
    prior_spam = (spam_count + pseudo_count) / (total_emails + pseudo_count * num_classes)

    return prior_spam


def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    header = training_examples[0]
    data = training_examples[1:]

    num_features = 12
    spam_counts = [0] * num_features
    not_spam_counts = [0] * num_features
    total_spam = 0
    total_not_spam = 0

    for row in data:
        features = row[:-1]
        label = row[-1]

        if label == '1':
            total_spam += 1
            for i in range(num_features):
                if features[i] == '1':
                    spam_counts[i] += 1
        else:
            total_not_spam += 1
            for i in range(num_features):
                if features[i] == '1':
                    not_spam_counts[i] += 1

    likelihood = []
    for i in range(num_features):
        prob_true_given_not_spam = (not_spam_counts[i] + pseudo_count) / (total_not_spam + 2 * pseudo_count)
        prob_true_given_spam = (spam_counts[i] + pseudo_count) / (total_spam + 2 * pseudo_count)
        likelihood.append((prob_true_given_not_spam, prob_true_given_spam))

    return likelihood


def posterior(prior, likelihood, observation):
    numerator_true = prior
    numerator_false = 1 - prior

    for i in range(len(observation)):
        obs = observation[i]

        p_xi_given_C_true = likelihood[i][True]
        p_xi_given_C_false = likelihood[i][False]

        if not obs:
            p_xi_given_C_true = 1 - p_xi_given_C_true
            p_xi_given_C_false = 1 - p_xi_given_C_false

        numerator_true *= p_xi_given_C_true
        numerator_false *= p_xi_given_C_false

    denominator = numerator_true + numerator_false
    posterior_true = numerator_true / denominator  

    return posterior_true


def nb_classify(prior, likelihood, input_vector):
    # Ensure input_vector elements are integers (0 or 1)
    input_vector = [int(x) for x in input_vector]
    
    # Convert the input vector elements to booleans (True or False)
    observation = [bool(x) for x in input_vector]
    
    # Compute the posterior probability of Class=True (Spam)
    posterior_spam = posterior(prior, likelihood, observation)
    
    # The posterior probability of Not Spam is 1 - posterior_spam
    posterior_not_spam = 1 - posterior_spam
    
    # Determine the predicted class and certainty
    if posterior_spam > posterior_not_spam:
        # If posterior probability of spam is higher, classify as 'Spam'
        label = "Spam"
        certainty = posterior_spam
    elif posterior_spam < posterior_not_spam:
        # If posterior probability of not spam is higher, classify as 'Not Spam'
        label = "Not Spam"
        certainty = posterior_not_spam
    else:
        # If probabilities are equal, default to 'Not Spam' as per the requirement
        label = "Not Spam"
        certainty = posterior_not_spam
    
    # Return the predicted label and the certainty
    return (label, certainty)


#test
FILE_PATH = "./lab9-machine-learning-naive-bayes-nets/spam-labelled.csv"

prior = learn_prior(FILE_PATH)
likelihood = learn_likelihood(FILE_PATH)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))
    
print('\n')

prior = learn_prior(FILE_PATH, pseudo_count=1)
likelihood = learn_likelihood(FILE_PATH, pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))