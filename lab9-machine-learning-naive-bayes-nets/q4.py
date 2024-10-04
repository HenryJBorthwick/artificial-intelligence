import csv

def learn_likelihood(file_name, pseudo_count=0):
    # Read the CSV file into training_examples
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    # Skip the header row
    header = training_examples[0]
    data = training_examples[1:]
    
    # Number of features X1 to X12
    num_features = 12
    
    # Initialize counts
    # Counts of X_i = True given Spam = True
    spam_counts = [0] * num_features      

    # Counts of X_i = True given Spam = False
    not_spam_counts = [0] * num_features  

    # Total number of spam emails
    total_spam = 0         

    # Total number of not-spam emails               
    total_not_spam = 0                   

    # Iterate over each email in the data
    for row in data:
        # All columns except the last one
        features = row[:-1]

        # Last column is the label (Spam: '1' or '0')
        label = row[-1]
        
        # Check if email is spam
        if label == '1':
            total_spam += 1

            # For each feature
            for i in range(num_features):
                if features[i] == '1':
                    spam_counts[i] += 1
        else:  
            
            # Email is not spam
            total_not_spam += 1
            
            # For each feature
            for i in range(num_features):
                if features[i] == '1':
                    not_spam_counts[i] += 1
    
    # Compute likelihood probabilities with Laplace smoothing
    likelihood = []
    for i in range(num_features):
        # For Spam = True
        # [True]: P(X_i = True | Spam = True)
        prob_true_given_spam = (spam_counts[i] + pseudo_count) / (total_spam + 2 * pseudo_count)
        # For Spam = False
        # [False]: P(X_i = True | Spam = False)
        prob_true_given_not_spam = (not_spam_counts[i] + pseudo_count) / (total_not_spam + 2 * pseudo_count)
        
        # Store probabilities in a tuple or list with indices [False] and [True]
        likelihood.append((prob_true_given_not_spam, prob_true_given_spam))
    
    return likelihood


#test
FILE_PATH = "./lab9-machine-learning-naive-bayes-nets/spam-labelled.csv"


likelihood = learn_likelihood(FILE_PATH)
print(len(likelihood))
print([len(item) for item in likelihood])

print('\n')

likelihood = learn_likelihood(FILE_PATH)

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

print('\n')

likelihood = learn_likelihood(FILE_PATH, pseudo_count=1)

print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))