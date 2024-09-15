% Do not change these facts:

% irina is a direct decendent of natasha
directlyIn(irina, natasha).
% natasha is a direct decendent of olga
directlyIn(natasha, olga).
% olga is a direct decendent of katarina
directlyIn(olga, katarina).

% parent(X, Y)

% Add the predicate `contains` here:
% decendent implementation.
% X is a direct decendent of Y IF X is a child of Y OR X is a child of Z AND Z is a indirect decendent of Y
contains(X, Y) :- directlyIn(Y, X).
contains(X, Y) :- directlyIn(Y, Z), contains(X, Z).


% descendant(X, Y) :- child(X, Y).                    
% X is a child of Z, and Z is a descendant of Y
% descendant(X, Y) :- child(X, Z), descendant(Z, Y).


% descendant(X, Y) :- parent(Y, X).
% Y is a parent of Z, and X is a descendant of Z
% descendant(X, Y) :- parent(Y, Z), descendant(X, Z).
