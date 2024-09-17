% prolog peano numerals positive

% base case: zero is not positive
natural(zero).

% recursive case: a number is positive, if it is a successor of another natural number (removes a succ each time)
natural(succ(X)) :- natural(X).

% Natural number, non-negative integer and not zero
positive(succ(X)) :- natural(X).

% strips off succ each loop