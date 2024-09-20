
reversed([], []).

reversed([H1|T1], Backwards) :- reversed(T1, ReversedTail), append(ReversedTail, [H1], Reversed).