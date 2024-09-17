% prolog find max of list

% Define the helper predicate to find the maximum of two numbers
max_of_two(X, Y, X) :- X >= Y.
max_of_two(X, Y, Y) :- Y > X.

% Define the max/2 predicate to find the maximum in a list
max([Head|Tail], Max) :-
    max_helper(Tail, Head, Max).

% Helper predicate that carries the current maximum
max_helper([], CurrentMax, CurrentMax).
max_helper([Head|Tail], CurrentMax, Max) :-
    max_of_two(Head, CurrentMax, NewMax),
    max_helper(Tail, NewMax, Max).
