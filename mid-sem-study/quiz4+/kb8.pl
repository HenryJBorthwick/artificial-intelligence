% prolog peano numerals add

% base case: zero
natural(zero).
% recusrive case: strips a succ off each time
natural(succ(X)) :- natural(X).


% base case: for add, where adding zero to Y results in Y
add(zero, Y, Y) :- natural(Y).

% recursive case: for add, add X+1 to Y, add X to Y to get Z
add(succ(X), Y, succ(Z)) :- add(X, Y, Z).
