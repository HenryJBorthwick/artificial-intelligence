


female(juliet).
parent(bob, juliet).
parent(bob, john).

% sister if parent1 and parent2 and female and no_equal(X,Y) 
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \= Y.

% X\=Y means: true if X does not equal Y