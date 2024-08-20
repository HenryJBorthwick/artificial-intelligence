

/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

/* no_lenses if person has low_tear_rate */
diagnosis(no_lenses, _Age, _Astigmatic, Tear_Rate) :- low_tear_rate(Tear_Rate).

/* soft_lenses if person is young and has normal tear rate and does not have astigmatism */
diagnosis(soft_lenses, Age, no, Tear_Rate) :- normal_tear_rate(Tear_Rate), young(Age).

/* hard_lenses if person is young and has normal tear rate and has astigmatism */
diagnosis(hard_lenses, Age, yes, Tear_Rate) :- normal_tear_rate(Tear_Rate), young(Age).