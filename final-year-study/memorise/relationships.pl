descendent(X,Y) :- child(X,Y).
descendent(X,Y) :- child(X,Z), descendent(Z,Y).

ascendent(X,Y) :- child(Y,X).
ascendent(X,Y) :- child(Y,Z), ascendent(X,Z).


% --- Asendent Tests ---
% child(irina, natasha).
% child(natasha, olga).
% child(olga, katarina).

test_child_irina_natasha :-
    child(irina, natasha),
    writeln('OK').
% Expected Output:
% OK

test_child_irina_olga :-
    \+ child(irina, olga),
    writeln('OK').
% Expected Output:
% OK

test_asendent_katarina_irina :-
    ascendent(katarina, irina),
    writeln('OK').
% Expected Output:
% OK

test_asendent_katarina_natasha :-
    ascendent(katarina, natasha),
    writeln('OK').
% Expected Output:
% OK

test_contains_all_asendent_irina :-
    findall(P, ascendent(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).
% Expected Output:
% katarina
% natasha
% olga

test_ascendent :-
    test_child_irina_natasha,
    test_child_irina_olga,
    test_asendent_katarina_irina,
    test_asendent_katarina_natasha,
    test_contains_all_asendent_irina.


% --- Desendent Tests ---
child(a, b).
child(b, c).
child(c, d).
child(e, d).


test_child_a_c :- 
    descendent(a, c),
    writeln('OK').
% Expected Output:
% OK


test_descendent_a_e :- 
    descendent(a, X),
    descendent(e, X),
    writeln(X).
% Expected Output:
% d

test_descendent :-
    test_child_a_c,
    test_descendent_a_e.
