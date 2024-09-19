/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = no_lenses, 
    low_tear_rate(Tear_Rate).

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = hard_lenses,
    young(Age),
    Astigmatic = yes,
    normal_tear_rate(Tear_Rate).


diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = soft_lenses,
    young(Age),
    Astigmatic = no,
    normal_tear_rate(Tear_Rate).
