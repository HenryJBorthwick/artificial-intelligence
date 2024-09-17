% prolog list merge, 

% Base Case 1: If ListA is empty, the merged list is ListB
merge([], ListB, ListB).   % Complete one of the two base cases

% Base Case 2: If ListB is empty, the merged list is ListA
merge(ListA, [], ListA).    % Complete the other base case

% Recursive Case: Both lists are non-empty
merge([X | ListA], [Y | ListB], [X | Merged]) :-
    % x less than y in list a and b
    X < Y,
    merge(ListA, [Y | ListB], Merged).


merge([X | ListA], [Y | ListB], [Y | Merged]) :-   % Complete the other rule
    % x greater than or equal to y in merged list
    X >= Y,
    merge([X | ListA], ListB, Merged).