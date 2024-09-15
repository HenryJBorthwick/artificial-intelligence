

% true if the two points equal each others value
reflect(point(X, Y)) :- X = Y.

% true if X1 = Y2 AND X2 = Y1 
reflection(point(X1, Y1), point(X2, Y2)) :- reflect(point(X1, Y2)), reflect(point(X2, Y1)).