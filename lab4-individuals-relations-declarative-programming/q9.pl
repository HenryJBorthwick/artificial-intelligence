% Do not change these facts:

directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).


/* DESCENDANT DEFINITION */
/*
descendant(X, Y) :- child(X, Y).
descendant(X, Y) :- child(X, Z), descendant(Z, Y).

THIS IS VERTICAL LINEAGE
*/

% Add the predicate `contains` here:

/* Is Y contained in X? */
/* BASE CASE: Y is a child of X */

/* if x is directly in Y, then Y contains X */
contains(X, Y) :- directlyIn(Y, X).

/* RECURSIVE CASE: */

/* if X is in Z and Z is in Y then Y also contains X */
contains(X, Y) :- directlyIn(Z, X), contains(Z, Y).

% THIS IS NESTED CONTAINMENT
