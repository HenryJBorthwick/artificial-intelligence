% prolog DNA matching
% reorganise list according to pair matching

% DNA pair rules
pair(a, t).
pair(c, g).

% check for DNA match according to DNA rules
match(X, Y) :- pair(X,Y); pair(Y, X).

% base case: empty lists
dna([], []).   

% recursive case: try match first two items, 
dna([H1|T1], [H2|T2]) :- match(H1, H2), dna(T1, T2).