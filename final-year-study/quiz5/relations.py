from csp import Relation

relations = [
    Relation(
        header=['a', 'b', 'c'],
        tuples={(2,1,0),(2,0,1),(2,0,0),(1,0,0)},
    ),

    Relation(
        header=['c', 'd'],
        tuples={(2,1),(2,0),(1,0)}
    ),
]


print(len(relations))
print(all(type(r) is Relation for r in relations))