TEST KNOWLEDGE ON HARD MULTICHOICE DFS, BFS, LCFS, A*

Consistent and Admissible implications for above



- DFS
  - Completeness: Guarantees to find a solution if one exists and there are no cycles
  - Optimality: Does not guarantee finding a lowest cost or shortest path solution. Can simply find a non optimal solution first.
  - Time Complexity: O(b^m), b = branching factor, m maximum depth of search tree, worst case it explores all nodes in the deepest path. 
  - Space Complexity: O(bm), Stores only nodes in current path
  - Admissibility and consistency does not apply as there is no heuristic to apply here.

- BFS
  - Completeness: Guarantees to find a solution. Explores all levels.
  - Optimality: Optimal if all step costs are equal, otherwise no as it considers only path length not cost
  - Time Complexity: O(b^(d+1)) BFS explores every node up to depth d, exponential
  - Space Complexity: O(b^(d+1)) BFS stores all nodes at every level up to depth d, exponential 
  - Admissibility and consistency, N/A as no heuristic function

- LCFS
  - Completeness: Given all costs are positive, which prevents infinite loops, then it will guarantee a solution
  - Optimality: Optimal as it expands nodes in order of increasing path cost
  - Time Complexity: O(b⌈C∗/ϵ⌉), C∗: Cost of the optimal solution. ϵ: Minimum action cost. Exponential. Number of nodes with cost less than or equal to C*.
  - Space Complexity: O(b⌈C∗/ϵ⌉). Exponential as must store all nodes explored.
  - Admissibility and consistency: N/A as no heuristic function

- A* 
  - Completeness: IF branching factor is finite, all steps costs are positive, and heuristic is admissible. Expands every node heuristic value is less than cost of optimal solution (hence being admissible)
  - Optimality: Optimal if heuristic is admissible and consistent
  - Time complexity: Worst case depends on accuracy of heuristic, but if bad will behave exponential in depth of solution.
  - Space complexity: Worst case exponential in depth of solution. Has to keep all nodes in memory.
  - Admissibility: Never over estimates true minimal or optimal cost to each goal from node n.
  - Consistency: Never over estimates the cost of getting to node plus the estimated cost to the goal
    - Consistency implies Admissibility