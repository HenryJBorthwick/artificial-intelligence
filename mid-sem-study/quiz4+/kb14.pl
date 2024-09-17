% prolog create mirror binary tree

% Base case: Both are leaf nodes with the same label
mirror(leaf(Label), leaf(Label)).

% Recursive case: Both are tree nodes
mirror(tree(Left1, Right1), tree(Left2, Right2)) :-
    mirror(Left1, Right2),
    mirror(Right1, Left2).
