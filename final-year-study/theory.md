# theory 

## Complete
- Guarantees to find a solution IF one exists

## Optimal solution
- Path with the fewest arcs

## time space complexity
- b = branching factor
- d = depth

## BFS
- Uses a queue frontier. Explores level by level. 
- Guarantee find optimal solution if it exists.
- Complete. Will always find a solution if it exists. (Will find solution on infinite graph if exists at finite depth)
- Halts on every finite graph. May not halt on infinite graphs with no solution.
- Complexity of time and space O(b^d)
- Not effected by the goal state

## DFS
- Uses a stack frontier. Explores path as deep as possible before backtracking. 
- Not guaranteed to find optimal solution. May find a non-optimal solution.
- Complete only on finite graphs with no cycles. (A cycle turns it into an infinite graph)
- Halts only on finite graphs with no cycles.
- Complexity of time O(b^d), Complexity of space O(b*d)
- Not effected by the goal state

- NOTE: That the even finite graphs can have areas not reachable or simply come to solution before their edge cases.

## Common BFS DFS


## Optimal solution
- path with the lowest cost path

## LCFS
- Uses a priority queue. Explores lowest cost paths so far.
- Guarantee to find optimal solution if it exists.
- Complete. Will always find a solution if it exists. (If pruning employed, may not return optimal solution)
- Halts on every finite graph with no zero cost cycles. (Zero costs turns into infinite graph, or infinite graph with infinity decreasing costs)
- Effected by goal state?
- To use pruning or no pruning is a trade off between optimality and efficiency

## A*
- Uses a priority queue. Explores lowest cost path so far considering the path cost and heuristic estimate.
- Heuristic function
  - Consistent, then admissible
- Guarantee to find optimal solution if heuristic function is consistent or admissible.
- Complete?
- Halts every finite graph with no zero cost cycles and uses a admissible heuristic function
- Effected by goal sate?
- Pruning does not effect a consistent heuristic function, does effect a admissible by no longer ensuring it will find optimal solution.