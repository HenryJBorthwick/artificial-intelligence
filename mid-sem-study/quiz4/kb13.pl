% prolog recursion tree traversel

% pre order traversel

% base case: hit leaf node as that is simplist form of tree and the traversal list is equal
preorder(leaf(Value), [Value]).

% recursive case: git leaf node as, backtrack up
preorder(tree(Root, Left, Right), [Root | Traversal]) :-
    % Pre order traversal
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, Traversal).