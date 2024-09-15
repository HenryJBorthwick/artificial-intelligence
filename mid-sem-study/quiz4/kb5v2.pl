/* Diagnositc clauses */
% no lenses if person has low tear rate
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = no_lenses, 
    Tear_Rate < 5.

% soft lenses if person is young AND has normal tear rate and no astigmatism
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = soft_lenses, 
    Age < 45, 
    Astigmatic = no, 
    Tear_Rate >= 5. 

% hard lenses if person has young AND normal tear rate and astigmatism
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = hard_lenses, 
    Age < 45, 
    Astigmatic = yes, 
    Tear_Rate >= 5. 