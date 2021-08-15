from collections import deque
# 
# Algorithms(steps) to search a graph/tree 
# -> Traversal => visit all nodes 
#
# Always start at the simplest and scale from there
# -> this avoids confusion and works well with recursion mindset
# -> usually a node with two children is a good start
#
# Recursive function to traverse a tree
# -> think about how to break down the tree into subtrees
# -> base case (the simplest case)
# -> logic to process current node
# -> recurse left and right (order matters) with/without the processed data
#    as input 
# -> whether to return value during backtracking for processing logic
# -> Backtracking => going back one level from child to parent; uses last-in-first-out concept

# class definition for creating Graph/Tree node
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Breadth first search (BFS)
# -> idea: visit your node's direct neighbors, then their neighbors until no neighbor(base case)
# -> base case(usually is recurse until None, out of bounds) vs 
# -> processing case(usually is a condition where we found a node or met a condition)
# -> either way, both base & processing case terminate recursion

# Iterative(using loops) BFS implementation using Queue
def iterative_bfs(root):
  current_level_queue = deque() 
  next_level_queue = deque() 

  # base case(until None or is already None)
  if root is None:
    return 
  
  current_level_queue.append(root) # insert node at right end
  while len(current_level_queue) > 0: 
    while len(current_level_queue) > 0:
      node = current_level_queue.popLeft() 
      
      # <insert code to process node>
      
      # add neighbors/children to next_level queue
      next_level_queue.append(node.left)
      next_level_queue.append(node.right)
    
    # current_level is now empty; time to process next_level_queue
    # use python way to swap, so next_level queue becomes empty while we continue
    # processing current_level, satisfying our outer while loop
    current_level_queue, next_level_queue = next_level_queue, current_level_queue

# TODO
def recursive_bfs(root):
  pass


# BFS Algorithm Pseudocode
# -> start with a node, and go to all its neighbors/children 
# -> when that is done, start going to its neighbors' neighbors
# -> repeat this until we have visited all nodes' neighbors


# Depth first search (DFS)
# -> idea: dive deep into 1 path until the end, then backtrack up one level and repeat
# -> separate this idea from the node processing step (preorder, postorder, inorder)

# DFS Algorithm Pseudocode
# -> start with a node, and go to its first child, then the child's first child
# -> repeat until you reach a leaf node(without any child)
# -> backtrack the last node and repeat the process

# Pre-order DFS (process root node first, then leaf nodes)
def preorder_dfs(root):
  # the input can also be called "node" if we're dealing with a general graph ds
  if root is None: # base case
    return
  
  print(root.val) # process root
  preorder_dfs(root.left) # recurse left
  preorder_dfs(root.right) # recurse right

# Post-order DFS (process leaf nodes first, then root node)
def postorder_dfs(root):
  if root is None:
    return 

  postorder_dfs(root.left) # recurse left
  postorder_dfs(root.right) # recurse right
  print(root.val) # process root

# In-order DFS (process left leaf nodes, then root node, then right leaf nodes)
def inorder_dfs(root):
  if root is None:
    return

  inorder_dfs(root.left) # recurse left
  print(root) # process root
  inorder_dfs(root.right) # recurse right 


# Dijkstra's Algorithm for Weighted graph