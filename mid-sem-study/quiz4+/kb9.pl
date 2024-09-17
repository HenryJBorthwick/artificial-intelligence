% prolog lists represented like peano numerals

/* Lists can be represented using a base case of an empty list
and a constructor functor, cons, to add elements to the list */

/*
list(empty).  % The atom 'empty' represents the empty list.
list(cons(Element, Tail)) :- list(Tail).  % If Tail is a list, then cons(Element, Tail) is also a list.
*/

% base case: empty list
list(empty).

% recursive case: strip a con each time
list(cons(_, Tail)) :- list(Tail).

% base case: empty lits for concat
concat(empty, B, B) :-
    list(B).

% recursive case: 
concat(cons(H, T), B, cons(H, AB_Tail)) :-
    concat(T, B, AB_Tail).