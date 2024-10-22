% all_distinct(+List)
% Succeeds if all elements in List are distinct.

all_distinct([]).  % An empty list has all distinct elements by definition.

all_distinct([Head|Tail]) :-
    \+ member(Head, Tail),  % Ensure Head is not a member of Tail.
    all_distinct(Tail).     % Recursively check the Tail.
