% Facts
%likes(bob, chocolate).
%hungry(alice).

edible(crisps).
hungry(bob).
likes(bob, sushi).

/* This example shows how our incomplete definition of
rules can lead to unexpected (nonsense) answers. */

%likes(alice, rock).
%likes(alice, jazz).
%edible(pizza).
%hungry(bob).

% Rules
% Person eats thing if that person likes that thing
eats(Person, Thing) :- likes(Person, Thing).

% Person eats thing if person is hungry and thing is edible
eats(Person, Thing) :- hungry(Person), edible(Thing).