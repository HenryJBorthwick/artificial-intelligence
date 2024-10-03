import csv

# def learn_prior(file_name, pseudo_count=0):
#     # Initialize counts
#     total_emails = 0
#     spam_count = 0

#     with open(file_name, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row

#         for row in reader:
#             total_emails += 1
#             label = row[-1]  # The last column is the label

#             if label == '1':
#                 spam_count += 1

#     # Number of classes (spam and not spam)
#     num_classes = 2

#     # Apply Laplace smoothing
#     prior_spam = (spam_count + pseudo_count) / (total_emails + pseudo_count * num_classes)

#     return prior_spam

def learn_prior(file_name, pseudo_count=0):
    # Read the CSV file into training_examples
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    # Skip the header row
    header = training_examples[0]
    data = training_examples[1:]
    
    # Initialize counts
    total_emails = len(data)
    spam_count = 0
    
    # Iterate over each example to count spam labels
    for row in data:
        # The last element is the label
        label = row[-1]  
        # Check if marked as spam email
        if label == '1':
            spam_count += 1
    
    # Number of classes (spam and not spam)
    num_classes = 2
    
    # Apply Laplace smoothing
    prior_spam = (spam_count + pseudo_count) / (total_emails + pseudo_count * num_classes)
    
    return prior_spam


#test
prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))

print('\n')

prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))

print('\n')

prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))

print('\n')

prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))

print('\n')

prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))

print('\n')

prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))

print('\n')

prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))