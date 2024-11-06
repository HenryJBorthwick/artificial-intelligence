preorder(leaf(X), X).
preorder(tree(X, Left, Right), [X|Traversal]) :-
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, Traversal).

inorder(leaf(X), X).
inorder(tree(X, Left, Right), Traversal) :-
    inorder(Left, LeftTraversal),
    inorder(Right, RightTraversal),
    append(LeftTraversal, [X|RightTraversal], Traversal).

postorder(leaf(X), X).
postorder(tree(X, Left, Right), Traversal) :-
    postorder(Left, LeftTraversal),
    postorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, TempTraversal),
    append(TempTraversal, [X], Traversal).

descendent(X,Y) :- child(X,Y).
descendent(X,Y) :- child(X,Z), descendent(Z,Y).

ascendent(X,Y) :- child(Y,X).
ascendent(X,Y) :- child(Y,Z), ascendent(X,Z).

knn:
Compute distance between input and input data
Add to distance, output data tuple
sort distances
get k_neighbors from distance
tie break k_neighbors, update their distances
extract distance, output data FROM k_neighbors and compute outcomes
use function/combine to compute prediction

ea:
compute fitness
compute cum fitness
compute norm cum fitness
loop through population and norm cum fitness
select r < norm cum fitness
return individual

min-max:
check if terminal node
init top util
loop through children of tree
get top util from opposite min or max
check if local top util greater or less than top util
update top util
return top util

optimal, then update to use game tree with (index, util)

binary classification:
activation = (w1*x1) + (w2*x2) + b >= 0 then y=1
error = t - y = 0 then no update

gac:
working through the values, is there a value that never satisfies it?
when domain changed second time, add to TODO set and process after
work through constraints both ways every time

relations:
find all possible values

variable eliminate:
get constraints with that variable
intersect common variables
join tuples where the intersection values match
remove the variable to eliminate from tuple

network:
a influences b, a->b, parent->variable

smoothing:
(parent_variable_condition + sudo_count)/(parent_condition+ sudo_count*num_states)

alpha-beta:
no pruning check on terminal nodes

consistency:
h(tail) <= h(head) + c(head->tail) (edge cost)

admissibility:
h(node) <= c(node->goal) (optimal path cost)


local, global search theory:
- local used for optimization problems within a finite space. (Search space)
- finds initial solution, moves to neighbors util satisfactory solution found
- Searching a space for higher or lowest point
  - Highest use hill climbing 
  - Lowest use gradient descent
- Local faster than exhaustive, but not guarantee of best solution,stuck in local optima, best solution compared to neighbors, but not globally. Random restart from new state and random step during search.
- Use in csp problems, minimize number of conflicts using heuristic function, which are unsatisfied constraints
- Global search covers entire search space rather than just neighbors.
- EA, mutation is random change to individual, cross over is two parent individual create offspring

belief network and joint distribution theory:
- belief networks use conditional independent to reduce local distribution into smaller, localized distributions.
- nodes = random variables which hold observed values or remain unobserved
- acrylic graph directed arcs represent potential dependencies or influences between variables
- CPT conditional probability distribution of variable node
- joint distributions, probability of every possible combination of values for a set of random variables. 

games theory:
- Monte carlo tree search, expand based on promising nodes based on simulated playouts. 

predicting sequences:
- expression trees, prefix notation, nested lists (root, left, right)

Algorithms:
min-max
ea
knn

greedy 
n_queens
gac