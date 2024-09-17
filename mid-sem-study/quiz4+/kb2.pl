% prolog manual append/3 implementation

% base case: empty list
% []: Represents an empty list.
% B: The second list remains unchanged.
% AB: When appending an empty list to B, the result is B.
new_append([], B, B).

% recursive case:
% [H|T]: Deconstructs list A into its head H and tail T.
% [H|AB]: Constructs the resulting list by placing H at the front, followed by the result of appending T to B.
% new_append(T, B, AB): Recursively appends the tail T to B, yielding AB.
new_append([H|T], B, [H|AB]) :-
    new_append(T, B, AB).
