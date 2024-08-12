/* Knowledge base given */
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X\=Y.

female(juliet).
parent(bob, juliet).
parent(bob, john).

