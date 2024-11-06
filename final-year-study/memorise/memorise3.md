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
    append(LeftTraversal, RightTraversal, TempTraversal).
    append(TempTraversal, [X], Traversal)

descendent(X,Y) :- child(X,Y).
descendent(X,Y) :- child(X,Z), descendent(Z,Y).

ascendent(X,Y) :- child(Y,X).
ascendent(X,Y) :- child(Y,Z), ascendent(X,Z).

ea:
compute fitness values
compute cumulative fitness values
compute normal cumulative fitness values
go through population and norm_cum_fit values and check if r < ncf value

knn:
compute distances between input and data input
put into tuple of distance and data output
get k_neighbors
tie break k_neighbors distances
extract outputs from k_neighbors and combine/perform prediction calculation

min-max:
check for terminal node
init top util
loop through tree
get util of opposite child
check util of opposite child is greater/less than top util
update top util
return top util

For optimal, update to use game tree of (index, util)

consistency:
h(tail) <= h(head) + c(tail->head) (edge cost)

admissibility:
h(node) <= c(node to goal) (optimal path cost)

binary update:
activation = (w1 * x1) + (w2 * x2) + b >= 0 then y=1
error = t - y = 0 then no update
w_new = w_old + (x1*n)(error)
b_new = b_old + (n)(error)

belief networks:
a influences b, then parent = a influences variable = b
smoothing:
(parent_variable_condition + sudo_count)/(parent_condition + sudo_count + num_states)

csp:
gac:
check under all conditions possible, what values never satisfy it
check both ways against constraint. 
carry over domain edits
if domain edited, add to todo set to process immediately after
when processing todo, make sure to do all domains and do both ways and add further updates

relations:
find possible value combinations
work through each constraint
set side of equality to one num and work through all other permutations

variable elimination:
get constraints with variables to eliminate
get intersection of common variables
join tuples on where common variables are same
remove the variable to eliminate from tuple

alpha-beta:
do not perform prune check on terminal nodes


