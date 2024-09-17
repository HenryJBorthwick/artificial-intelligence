%  prolog binary digit match

% regex: 0b(0|1)+. 
% translation: first digit 0, second digit b, followed by at least 1 either 0 or 1

%  check if digit is zero or one
zero_or_one(D):- D = 0; D =1. 

% checks if the rest of string is binary
zero_or_one_sequence([H|T]) :- zero_or_one(H), (T=[]; zero_or_one_sequence(T)).


% main function call
binary_number([0, b | Ds]) :- 
    % check at least 1 digit, check not empty list
    Ds \= [],
    % check if remaing digits are 0 or 1 digits
    zero_or_one_sequence(Ds).