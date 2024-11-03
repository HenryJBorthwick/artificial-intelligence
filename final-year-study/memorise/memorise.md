
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
    append(LeftTraversal, RightTraversal, TempTraversal)
    append(TempTraversal, [X], Traversal).

desendent(X, Y) :- child(X, Y).
desendent(X, Y) :- child(X, Z), desendent(Z, Y).

asendent(X, Y) :- child(Y, X).
asendent(X, Y) :- child(Y, Z), asendent(X, Z).

consistent
h(tail) <= h(head) + c(tail->head) (Edge Cost)

admissible
h(node) <= c(node->goal) (Optimal Path Cost)

Network Update
(Variable_True + SudoCount) / (Variable_Parent_Condition + SudoCount * number of states)

Binary Update
Activation = w * i + b >= 0 then y=1
Error = t - y = 0 then no update
Calculate Weight and Bias
