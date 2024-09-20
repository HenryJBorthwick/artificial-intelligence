
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


descendent(X, Y) :- child(X, Y).
descendent(X, Y) :- child(X, Z), descendent(Z, Y).

ansestor(X, Y) :- parent(Y, X).
ansestor(X, Y) :- parent(Y, Z), ansestor(X, Z).

consistent:
each edge
h(tail) <= h(head) + c(tail->head)

admissible:
each nodes optimal path to goal
h(node) <= c(path(node->goal))

- PROLOG
- Twice
- Translate

- Swap12
- Binary