from csp import Relation

relations = [
    Relation(header=['a', 'b', 'c'],
             tuples={(1, 0, 0), (2, 0, 0), (2, 0, 1), (2, 1, 0)}),

    Relation(header=['c', 'd'],
             tuples={(1, 0), (2, 0), (2, 1)})
]


relations = [
      
      Relation(header=['a', 'b'], tuples={(-1,-1), (1,1)}),

      Relation(header=['b', 'c'], tuples={(0,1), (1,0), (1,1)})
      
      ] 

relations_after_elimination = [
    
    Relation(header=['a', 'c'], tuples={(1,0), (1,1)})
    
    ] 