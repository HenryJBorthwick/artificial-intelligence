# things to note
- uses priority queue
- calculate path cost combining cost of each pair of nodes
- always pop the lowest cost path
- with pruning, update set of visited nodes with the end node each time a node is removed
  - when you pop a path who's end node is in the set visited add ! mark
  - if the path you are about to add has the end node in the set add ! mark and don't add to data structure
- when you have things of the same cost in lcfs then you pop the first added assuming alphabetical order