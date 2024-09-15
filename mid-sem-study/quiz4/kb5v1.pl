/* tear rate related clauses */
% if tear rate before or equal to 5, then its normal
normal_tear_rate(RATE) :- RATE >= 5.
% if tear rate is less than 5, then its low
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
% if age is below 45, age is young
young(AGE) :- AGE < 45.

/* Astigmatic clauses */
% astigmatic if astigmatic is yes
astigmatic(ASTIGMATIC) :- ASTIGMATIC = yes.

% not astigmatic, of astigmatic is no
not_astigmatic(ASTIGMATIC) :- ASTIGMATIC = no.

/* Reccomended lenses clauses*/
% no lenses, if reccomended is no_lenses
no_lenses(RECCOMENDED) :- RECCOMENDED = no_lenses.

% soft lenses, if reccomended is soft_lenses
soft_lenses(RECCOMENDED) :- RECCOMENDED = soft_lenses.

% hard lenses, if reccomended is hard_lenses
hard_lenses(RECCOMENDED) :- RECCOMENDED = hard_lenses.


/* Diagnositc clauses */
% no lenses if person has low tear rate
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    no_lenses(Recommend), 
    low_tear_rate(Tear_Rate).

% soft lenses if person is young AND has normal tear rate and no astigmatism
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    soft_lenses(Recommend), 
    young(Age), 
    not_astigmatic(Astigmatic), 
    normal_tear_rate(Tear_Rate).

% hard lenses if person has young AND normal tear rate and astigmatism
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    hard_lenses(Recommend), 
    young(Age), 
    astigmatic(Astigmatic), 
    normal_tear_rate(Tear_Rate).