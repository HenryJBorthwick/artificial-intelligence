preorder(leaf(X), [X]).
preorder(tree(X, Left, Right), [X|Traversal]) :-
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, Traversal).

inorder(leaf(X), [X]).
inorder(tree(X, Left, Right), Traversal) :-
    inorder(Left, LeftTraversal),
    inorder(Right, RightTraversal),
    append(Left, [X|RightTraversal], Traversal).

postorder(left(X), [X]).
postorder(tree(X, Left, Right), Traversal) :-
    postorder(Left, LeftTraversal),
    postorder(Right, RightTraversal),
    append()

postorder(leaf(X), [X]).
postorder(tree(X, Left, Right), Traversal) :-
    postorder(Left, LeftTraversal),
    postorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, TempTraversal),
    append(TempTraversal, [X], Traversal).

desendent(X,Y) :- child(X,Y).
desendent(X,Y) :- child(X,Z), desendent(Z,Y).

ascendent(X,Y) :- child(Y,X).
ascendent(X,Y) :- child(Y,Z), ascendent(X,Z).

consistency:
h(tail) <= h(head) + cost(tail->head) (edge cost)

admissibility:
h(node) <= cost(node->goal) (optimal path cost)