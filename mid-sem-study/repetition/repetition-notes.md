# quiz 1
- Frontier trace: edge list is directional, don't add to trace if not in right direction
- DFS Frontier Implementation, don't forget in the next to check length and raise StopIteration 

- DFS, BFS Trace + Implementation 
- Funky Graph (Do again)


# quiz 2
- LCFS trace With and Without pruning
- A* trace with and without pruning

- THEORY:
- (Tail -> Head)
- Consistency ensures that the heuristic value of the tail is less than or equal to the heuristic value of the head plus the edge cost
- Admissibility ensures that the heuristic value of the tail is less than or equal to the optimal path cost from the tail to the goal node
  - Goal node has a optimal path cost of 0
- CONSISTENCY ensures optimal path expansion. Expand as few paths as possible.
- ADMISSIBILITY ensures optimal path to goal expansion. Achieve lowest possible path from start to goal node.
- LCFS always finds optimal solution
- Pruning can produce non-optimal solutions if not admissible and consistent

- location graph (do again)
- LCFS frontier implementation (do again)


# quiz 3
- atoms are propositional variable
- interpretation functions are propositional statements with truth values assigned
- models are the collection of assignment that make all the propositional statements true

- kb theory questions, both propositional formula and propositional definite clauses

- TODO: Code questions

# quiz4
- turn equation into english
  - conclusion, conditions
  - inverse implies
- find the models
- descendant/ascendent relationships
- % ancestor definitions
```
% ancestor(X, Y) :- parent(X, Y).
% ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```
- % descendant definitons
```
% descendant(X, Y) :- child(X, Y).
% descendant(X, Y) :- child(X, Z), descendant(Z, Y).
```
- NOTE: Can use descendant and turn into acsendent using child(X, Y) :- parent(Y, X).
- list doubler (do again)
- translate (do again)


# EXTRA
- Pruning, implement, add to set considered
```            
    if head not in self.visited:
        self.visited.add(head)
        self.expanded.append(path)
        return path
```
- A*, get add cost and heuristic value together