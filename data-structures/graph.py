# Graph can be represented 2 ways:
#   1. Adjacency List 
#      -> a dictionary of all nodes (vertices), and for each node key,
#         a list of the nodes that it connects to
#      -> efficiently represent sparse graphs
#      -> Space = O(V + E)
#      -> Operations Run time
#         -> Adding a vertex and edge = O(1)
#         -> Deleting a vertex = O(E)
#         -> Deleting an edge = O(V)
#
#   2. Adjacency Matrix
#      -> a V x V matrix using 2D array with a boolean value indicating
#         if there is an edge between two vertices
#      -> efficiently represent dense graphs
#      -> Space = O(V x V)
#      -> Operations Run time
#         -> Adding/Deleting a vertex = O(V x V)
#         -> Adding/Removing an edge = O(1)