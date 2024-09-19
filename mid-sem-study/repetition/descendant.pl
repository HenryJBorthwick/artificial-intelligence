

% descendant definitons
% descendant(X, Y) :- child(X, Y).
% descendant(X, Y) :- child(X, Z), descendant(Z, Y).

% descendant(X, Y) :- parent(Y, X).
% descendant(X, Y) :- parent(Y, Z), descendant(X, Z).


% ancestor definitions
% ancestor(X, Y) :- parent(X, Y).
% ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% ancestor(X, Y) :- child(Y, Z).
% ancestor(X, Y) :- child(Y, Z), ancestor(X, Z).


% Parent Relationships
parent(john, mary).
parent(john, robert).
parent(mary, susan).
parent(mary, linda).
parent(susan, james).
parent(linda, peter).
parent(robert, emma).

% Child Relationships (Inverse of Parent)
child(mary, john).
child(robert, john).
child(susan, mary).
child(linda, mary).
child(james, susan).
child(peter, linda).
child(emma, robert).
