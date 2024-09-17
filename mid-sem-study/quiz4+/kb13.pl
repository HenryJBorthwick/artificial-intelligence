% prolog sort a list into a ordered list

% ----------------------------------------
% Helper Predicate: split_odd_even/3
% Splits a list into two lists: one with odd-indexed elements and one with even-indexed elements.
% ----------------------------------------

% Base case: Empty list
split_odd_even([], [], []).

% Base case: Single element list
split_odd_even([OddElement], [OddElement], []).

% Recursive case: List with two or more elements
split_odd_even([OddElement, EvenElement | Rest], [OddElement | RestOdds], [EvenElement | RestEvens]) :-
    split_odd_even(Rest, RestOdds, RestEvens).


% ----------------------------------------
% Helper Predicate: merge/3
% Merges two sorted lists into one sorted list.
% ----------------------------------------

% Base Case 1: If ListA is empty, the merged list is ListB
merge([], ListB, ListB).   % Complete one of the two base cases

% Base Case 2: If ListB is empty, the merged list is ListA
merge(ListA, [], ListA).    % Complete the other base case

% Recursive Case: Both lists are non-empty
merge([X | ListA], [Y | ListB], [X | Merged]) :-
    % x less than y in list a and b
    X < Y,
    merge(ListA, [Y | ListB], Merged).

merge([X | ListA], [Y | ListB], [Y | Merged]) :-   % Complete the other rule
    % x greater than or equal to y in merged list
    X >= Y,
    merge([X | ListA], ListB, Merged).

% ----------------------------------------
% Main Predicate: merge_sort/2
% Sorts a list of integers in ascending order using merge sort.
% ----------------------------------------

% Write the rules for merge
% Write the rules for split_odd_even

merge_sort([], []).  % Complete base case for the empty list
merge_sort([X], [X]). % Complete the base for a list with only one element

merge_sort(List, Sorted):-
	List = [_,_|_],    % the list has two or more elements
	split_odd_even(List, SubSeq1, SubSeq2),  % create two subproblems (divide)
	merge_sort(SubSeq1, SortedSeq1), % Complete (solve)
	merge_sort(SubSeq2, SortedSeq2),  % Complete (solve)
	merge(SortedSeq1, SortedSeq2, Sorted).   % Complet (combine)