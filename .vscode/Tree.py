""" 
Trees Introduction
Trees are an essential data structure for storing hierarchical data with a directed flow.

Similar to linked lists and graphs, trees are composed of nodes which hold data. The diagram represents nodes as circles and data as text.

Nodes also store references to zero or more other tree nodes. Data moves down from node to node. 
We depict those references as lines drawn between circles.

Trees are often displayed with a single node at the top and connected nodes branching downwards.

#Note - When a node has no children, we refer to it as a leaf node.
Trees grow downwards in computer science, and a root node is at the very top. The root of this tree is /photos.

Tree Varietals
Trees come in various shapes and sizes depending on the dataset modeled.

Some are wide, with parent nodes referencing many child nodes.

Some are deep, with many parent-child relationships.

Trees can be both wide and deep, but each node will only ever have at most one parent; otherwise, they wouldn't be trees!

Each time we move from a parent to a child, we're moving down a level.
Depending on the orientation we refer to this as the depth (counting levels down from the root node) or height (counting levels up from a leaf node).

••••••••••••••••••••
Binary Search Tree •
••••••••••••••••••••
Constraints are placed on the data or node arrangement of a tree to solve difficult problems like efficient search.

A binary tree is a type of tree where each parent can have no more than two children, known as the left child and right child.

Further constraints make a binary search tree:

Left child values must be lesser than their parent.
Right child values must be greater than their parent.

The constraints of a binary search tree allow us to search the tree efficiently. At each node, we can discard half of the remaining possible values!

Let's walk through locating the value 31.

Start at the root: 39
31 < 39, we move to the left child: 23
23 < 31, we move to the right child: 35
31 < 35, we move to the left child: 31
We found the value 31!
In a dataset of fifteen elements, we only made three comparisons. What a deal!

"""

class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


