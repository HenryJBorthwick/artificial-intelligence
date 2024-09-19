twice([], []).
twice([H|T], [H, H | T2]) :-
    twice(T, T2).
