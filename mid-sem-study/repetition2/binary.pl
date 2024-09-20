

zero_or_one([]).
zero_or_one([H|T]) :- zero_or_one(H), zero_or_one(T).
zero_or_one(0).
zero_or_one(1).


binary_number([0, b | Digits]) :- 
    Digits \= [],
    zero_or_one(Digits).