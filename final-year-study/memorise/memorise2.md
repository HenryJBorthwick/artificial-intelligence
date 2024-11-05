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

weight update:
Activation = (w1 * x1) + (w2 * x2) + b >= 1 then y = 0
Error = t - y = 0 then no update
w_new = w_old * n*x1 * Error
b_new = b_old * n * Error

# csp gac
# draw constraint
# check for satisfaction
# if eliminate, add to TODO set if not first time
# process todo if need be
# carry over edited domains where possible

# csp relations
# find all possible combinations that satisfy constraint

# csp variable elimination 
# get all constraints with variable to eliminate
# perform intersection between constraints for variables
# join the tuples where the intersection of variables are equal
# remove the variable to be eliminated from tuple

# min-max
# check terminal
# init util
# loop through tree
# get util
# compare util and update if better
# return best util
# update knowing that game_tree has action, util not just util now

# alpha-beta
# no update on terminal nodes

# ea
# compute fitness
# compute cum_fit
# compute total fitness
# compute norm_cum_fit
# select r < norm_cum_fit

# belief networks
# P(Variable=True|Parent=True or False)
# b influences e = b -> e = parent -> variable

# belief networks laplacian
# P(var_parent_condition + sudocount) / (parent_condition + sudocount * number states)

