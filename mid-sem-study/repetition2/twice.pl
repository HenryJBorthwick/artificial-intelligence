
% base case is simply always empty list
twice([], []).

% parameter one is input list, parameter two is the output list we want.
% the first part is the operator part, then the rest is a call to perform that operation
% on the rest of the list
twice([H1|T1], [H1, H1|Rest]) :- twice(T1, Rest).

twice([], []).
twice([H1|T1], [H1, H1|T2]) :- twice(T1, T2).