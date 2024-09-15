/* Comment */

% Comment 

%test1
% likes(bob, chocolate).
% hungry(alice).

%test2
edible(crisps).
hungry(bob).
likes(bob, sushi).

%test3


% Rule 1: A person eats something if the person likes that thing
% Condition (Antecedent): The person likes the thing.
% Conclusion (Consequent): The person eats the thing.
% Conclusion :- Condition
eats(Person, Thing) :- likes(Person, Thing).


% Rule 2: A person eats something if the person is hungry and that thing is edible
% Conditions (Antecedents):
    % The person is hungry.
    % The thing is edible.

% Conclusion (Consequent): The person eats the thing.
eats(Person, Thing) :- hungry(Person), edible(Thing).

% :- is a if
% , is a AND