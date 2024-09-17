% prolog cartesian product

% ----------------------------------------
% Helper Predicate: product/3
% Pairs a single element X with every element in ListB to form a list of tuples.
% ----------------------------------------

% The following helper predicate multiplies a single element by a list
product(_, [], []).   % base case
product(X, [H|T], [(X, H) | MorePairs]) :- product(X, T, MorePairs). % Complete


% ----------------------------------------
% Main Predicate: cartesian_product/3
% Forms the Cartesian product of two lists A and B.
% ----------------------------------------
cartesian_product([], _, []).
cartesian_product([Head|Tail], ListB, AllPairs) :-
    product(Head, ListB, HeadPairs),
    cartesian_product(Tail, ListB, RemainingPairs),  % Complete
    append(HeadPairs, RemainingPairs, AllPairs).  % Complete