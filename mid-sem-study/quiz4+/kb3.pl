% prolog bi-directional list reversal 

% base case: empty lists
reversed([], []).

% recursive case: 
reversed([H|T], Reversed) :-
    reversed(T, ReversedTail),
    append(ReversedTail, [H], Reversed).

% append 3 works by:
% - append(list1, list2, result)
% - IF list1 empty result is just list2
% - IF list1 not empty, Head of list1 pre-pended to result, recusivly appending the tail of list1 with list2

% DEFINITION?
% append([], L, L).
% append([H|T], L, [H|R]) :- append(T, L, R).
