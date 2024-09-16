% Prolog list extract


% second element of list IF list is greater >= 2 items, 
% base case if equal
% recursive case that iterates to next item in list and if you are over 2 items

% second element of list IF list is greater >= 2 items OR the second item does match 
second([_, X | _], X).
% List seperated into head and tail by the | operator
% _ operator can be anything