% prolog list recursion, didirection

% translation facts
tran(tahi,one). 
tran(rua,two). 
tran(toru,three). 
tran(wha,four). 
tran(rima,five). 
tran(ono,six). 
tran(whitu,seven). 
tran(waru,eight). 
tran(iwa,nine).

% base case: both empty lists
listtran([], []).

% recursive case: language 1 to language 2
listtran([H1|T1], [H2|T2]) :-
    % translate first element of each list
    tran(H1, H2),
    % countinue to translate rest of list elements
    listtran(T1, T2).

% recursive case: language 1 to language 2
listtran([H1|T1], [H2|T2]) :-
    % input maori and get english variable
    tran(H2, H1),
    listtran(T1, T2).

% pattern of extract elements, countiue with rest of list
% elements added from concationation of completed recusrion.