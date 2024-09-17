% prolog split list into list of elements with odd index and list of elements with even index

% Base case: Empty list
split_odd_even([], [], []).

% Base case: Single element list
split_odd_even([OddElement], [OddElement], []).

% Recursive case: List with two or more elements
split_odd_even([OddElement, EvenElement | Rest], [OddElement | RestOdds], [EvenElement | RestEvens]) :-
    split_odd_even(Rest, RestOdds, RestEvens).
