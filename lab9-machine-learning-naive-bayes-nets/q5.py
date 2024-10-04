import csv
import math

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


def posterior(prior_spam, likelihood, input_vector):
    # Initialize log probabilities with the log of prior probabilities
    log_prob_spam = math.log(prior_spam)
    log_prob_not_spam = math.log(1 - prior_spam)
    
    # Iterate over each feature in the input vector
    for i in range(len(input_vector)):
        # Current feature value (0 or 1)
        xi = input_vector[i]  
        
        # Likelihoods for the current feature given each class
        p_xi_given_not_spam, p_xi_given_spam = likelihood[i]
        
        if xi == 1:
            # If feature is present, add log likelihoods
            log_prob_spam += math.log(p_xi_given_spam)
            log_prob_not_spam += math.log(p_xi_given_not_spam)
        else:
            # If feature is absent, add log of (1 - likelihood)
            log_prob_spam += math.log(1 - p_xi_given_spam)
            log_prob_not_spam += math.log(1 - p_xi_given_not_spam)
    
    # Exponentiate log probabilities to get back to probability scale
    prob_spam = math.exp(log_prob_spam)
    prob_not_spam = math.exp(log_prob_not_spam)
    
    # Normalize probabilities so they sum to 1
    total_prob = prob_spam + prob_not_spam
    posterior_spam = prob_spam / total_prob
    posterior_not_spam = prob_not_spam / total_prob
    
    # Return posterior probabilities for both classes
    return posterior_spam, posterior_not_spam


def nb_classify(prior, likelihood, input_vector):
    # Ensure all features are integers
    input_vector = [int(x) for x in input_vector] 

    posterior_spam, posterior_not_spam = posterior(prior, likelihood, input_vector)

    if posterior_spam > posterior_not_spam:
        return ("Spam", posterior_spam)
    else:
        return ("Not Spam", posterior_not_spam)


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