
check(X, Y) :- X = Y.

reflection(point(X1, Y1), point(X2, Y2)) :- check(X1, Y2), check(X2, Y1).