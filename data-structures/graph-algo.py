# Algorithms(steps) to search a graph/tree 
#
# Always start at the simplest and scale from there
# -> this avoids confusion and works well with recursion mindset
# -> usually a node with two children is a good start
#
# Breadth first search (BFS)
# -> start with a node, and go to all its neighbors 
# -> when that is done, start going to its neighbors' neighbors
# -> repeat this until we have visited all nodes' neighbors

# Depth first search (DFS)
# -> start with a node, and go to its first child, then the child's first child
# -> repeat until you reach a leaf node(without any child)
# -> backtrack the last node and repeat the process

# Dijkstra's Algorithm for Weighted graph