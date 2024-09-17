% prolog list swap end elements

% Predicate to swap the first and last elements of a list

% Get the first and last element of list
swap_ends([First|Rest1], [Last|Rest2]) :-
    % split rest1 into middle and last
    append(Middle, [Last], Rest1),
    % split rest2 into middle and first
    append(Middle, [First], Rest2).
