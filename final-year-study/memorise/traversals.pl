preorder(leaf(X), [X]).
preorder(tree(X, Left, Right), [X|Traversal]) :-
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, Traversal).

inorder(leaf(X), [X]).
inorder(tree(X, Left, Right), Traversal) :-
    inorder(Left, LeftTraversal),
    inorder(Right, RightTraversal),
    append(LeftTraversal, [X|RightTraversal], Traversal).

postorder(leaf(X), [X]).
postorder(tree(X, Left, Right), Traversal) :-
    postorder(Left, LeftTraversal),
    postorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, TempTraversal),
    append(TempTraversal, [X], Traversal).

% --- Pre-order Tests ---

% Test 1: Single Leaf Node
test_preorder_leaf_a :-
    preorder(leaf(a), L),
    writeln(L).
% Expected Output:
% [a]

% Test 2: Complex Tree Structure
test_preorder_complex_tree :-
    preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
    writeln(T).
% Expected Output:
% [a, b, c, d, e]

% Test 3: Specific Expected Output
test_preorder_specific_output :-
    preorder(tree(x, leaf(z), leaf(q)), [x, z, q]),
    writeln('OK').
% Expected Output:
% OK

% Run All In-order Tests
test_preorder :-
    test_preorder_leaf_a,
    test_preorder_complex_tree,
    test_preorder_specific_output.


% --- In-order Tests ---

% Test 1: Single Leaf Node
test_inorder_leaf_a :-
    inorder(leaf(a), L),
    writeln(L).
% Expected Output:
% [a]

% Test 2: Complex Tree Structure
test_inorder_complex_tree :-
    inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
    writeln(T).
% Expected Output:
% [c, b, d, a, e]

% Test 3: Specific Expected Output
test_inorder_specific_output :-
    inorder(tree(x, leaf(z), leaf(q)), [z, x, q]),
    writeln('OK').
% Expected Output:
% OK

% Run All In-order Tests
test_inorder :-
    test_inorder_leaf_a,
    test_inorder_complex_tree,
    test_inorder_specific_output.


% --- Post-order Tests ---

% Test 1: Single Leaf Node
test_postorder_leaf_a :-
    postorder(leaf(a), L),
    writeln(L).
% Expected Output:
% [a]

% Test 2: Complex Tree Structure
test_postorder_complex_tree :-
    postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
    writeln(T).
% Expected Output:
% [c, d, b, e, a]

% Test 3: Specific Expected Output
test_postorder_specific_output :-
    postorder(tree(x, leaf(z), leaf(q)), [z, q, x]),
    writeln('OK').
% Expected Output:
% OK

% Run All In-order Tests
test_postorder :-
    test_postorder_leaf_a,
    test_postorder_complex_tree,
    test_postorder_specific_output.
