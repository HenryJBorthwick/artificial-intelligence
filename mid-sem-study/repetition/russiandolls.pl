% Do not change these facts:


directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).


% contains(X, Y) :- child(X, Y).
% contains(X, Y) :- child(X, Z), contains(Z, Y).

% child(X, Y) :- directlyIn(Y, X).




% contains(X, Y) :- directlyIn(Y, X).
% contains(X, Y) :- directlyIn(Y, Z), contains(X, Z).