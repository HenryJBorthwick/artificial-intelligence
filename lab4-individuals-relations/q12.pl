/* Translation facts */
tran(tahi,one).
tran(rua,two).
tran(toru,three).
tran(wha,four).
tran(rima,five).
tran(ono,six).
tran(whitu,seven).
tran(waru,eight).
tran(iwa,nine).

% Base case: translating two empty lists.
listtran([], []).

% Recursive case: translate the head of the list and then recursively translate the tail.
listtran([H1|T1], [H2|T2]) :- tran(H1, H2), listtran(T1, T2).
% Translate the head element using tran/2
% Recursively translate the tail