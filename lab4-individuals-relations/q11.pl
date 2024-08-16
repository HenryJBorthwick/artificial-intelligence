% Base case: The output for an empty input list is an empty output list.
twice([], []).

% Recursive case: Take the head of the input list, duplicate it in the output,
% and then recursively process the tail.
twice([H|T], [H,H|T2]) :- twice(T, T2).
