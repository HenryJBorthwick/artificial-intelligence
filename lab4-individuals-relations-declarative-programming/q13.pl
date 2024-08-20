% Base case: A leaf node.
preorder(leaf(X), [X]).

% Recursive case: A tree with a root, left subtree, and right subtree.
preorder(tree(Root, Left, Right), Traversal) :-
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append([Root | LeftTraversal], RightTraversal, Traversal).
