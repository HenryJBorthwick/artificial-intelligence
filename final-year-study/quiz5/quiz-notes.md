# notes

# arc consistency
- draw constraint
- eliminate what can't be reached, check for single satisfaction, do both ways
- if you eliminate, if its not the first time, then update other domains, but also perform the checks again
- carry over new domain where possible
- todo is a set of domains that need to be updated

# relations
- work through each constraint, find possible values
- trick is to pick variable on side of equality and work through range of possible values

# variable eliminations
- join the relations tuples on the intersection of all the relations that contain that variable to be eliminated
- when actually joining, join where all the variables match, then remove that variable to be eliminated from the tuple
- finally when writing the relations make sure to not include that variable and merge the relations