% prolog recursion tree traversel

% Preorder traversel

% base case: hit leaf node as that is simplist form of tree and the traversal list is equal
preorder(leaf(Value), [Value]).

% recursive case: get leaf node as, backtrack up
preorder(tree(Root, Left, Right), [Root | Traversal]) :-
    % Pre order traversal of left subtree
    preorder(Left, LeftTraversal),
    % Pre order traversal of rightsubtree
    preorder(Right, RightTraversal),
    % Concatenates left and right traversal lists using built in append
    append(LeftTraversal, RightTraversal, Traversal).


% inorder traversal

% base case: leaf node
inorder(leaf(Value), [Value]).

% recursive case: internal node
inorder(tree(Root, Left, Right), Traversal) :-
    % Inorder traversal of left subtree
    inorder(Left, LeftTraversal),
    % Inorder traversal of right subtree
    inorder(Right, RightTraversal),
    % Concatenates left traversal, root, and right traversal
    append(LeftTraversal, [Root | RightTraversal], Traversal).


% postorder traversal

% base case: leaf node
postorder(leaf(Value), [Value]).

% recursive case: internal node
postorder(tree(Root, Left, Right), Traversal) :-
    % Postorder traversal of left subtree
    postorder(Left, LeftTraversal),
    % Postorder traversal of right subtree
    postorder(Right, RightTraversal),
    % Concatenates left traversal, right traversal, and root
    append(LeftTraversal, RightTraversal, SubTraversal),
    append(SubTraversal, [Root], Traversal).
