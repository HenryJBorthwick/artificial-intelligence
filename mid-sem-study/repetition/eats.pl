eats(Person, Thing) :- likes(Person, Thing).
eats(Person, Thing) :- hungry(Person), edible(Thing).

likes(bob, chocolate).
hungry(alice).
edible(crisps).
hungry(bob).
likes(bob, sushi).

likes(alice, rock).
likes(alice, jazz).
edible(pizza).
hungry(bob).