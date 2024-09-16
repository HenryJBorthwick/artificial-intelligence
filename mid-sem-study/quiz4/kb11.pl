% prolog list recursion

% base case: empty left list
twice([], []).

% recusive case: extract stuff from output, IF rest of left list not empty and 
twice([H|T], [H, H| OutTail]) :- twice(T, OutTail).