"""
Linked List Introduction
Linked lists are one of the basic data structures used in computer science. 
They have many direct applications and serve as the foundation for more complex data structures.

The list is comprised of a series of nodes as shown in the diagram. The head node is the node at the beginning of the list. 
Each node contains data and a link (or pointer) to the next node in the list. The list is terminated when a node's link is null. 
This is called the tail node.

Consider a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). 
In this example, the initial departure city is the head node and the final arrival city is the tail node.

Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. 
These links also allow for quick insertion and removal of nodes as you will see in future exercises.

Common operations on a linked list may include:

adding nodes
removing nodes
finding a node
traversing (or travelling through) the linked list
Linked lists typically contain unidirectional links (next node), but some implementations make use of bidirectional links (next and previous nodes).

Can you think of a real world example using bidirectional links?

********************************************************************************************************************************************

Linked List Example
As an example, we added values to the linked list diagram from the introduction.

This linked list contains three nodes (node_a, node_b, and node_c).

Each node in this particular list contains an integer as its data. As the sequence is defined, the order is 3, 1, 20.

The list ends at node_c, since the link within that node is set to null.

What links would need to be established to add a new head node to this list? What about the tail?

********************************************************************************************************************************************
Linked Lists Adding and Removing Nodes
With linked lists, because nodes are linked to from only one other node, 
you can't just go adding and removing nodes willy-nilly without doing a bit of maintenance.

#Adding a new node

Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way,
you maintain your connection with the following nodes in the list.

#Removing a node

If you accidentally remove the single link to a node, that node's data and any following nodes could be lost to your application,
leaving you with orphaned nodes.

To properly maintain the list when removing a node from the middle of a linked list, 
you need to be sure to adjust the link on the previous node so that it points to the following node.

Depending on the language, nodes which are not referenced are removed automatically. 
"Removing" a node is equivalent to removing all references to the node.
"""

class Node:

    def __init__(self,value,next_node=None):
        self._value=value
        self._next_node = next_node

    def get_value(self):
        return self._value 
    
    def get_next_node(self):
        return self._next_node
    
    def set_node(self,new_node):
        self._next_node = new_node


class LinkedList:

    def __init__(self,value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self,new_value):
        new_node = Node(new_value)
        new_node.set_node(self.head_node)
        self.head_node = new_node
    
    def showLinkedList(self):
        current_head_node  =  self.get_head_node()
        newArray = []
        while current_head_node:
            if current_head_node.get_value() != None:
                newArray.append(current_head_node.get_value())
            current_head_node =  current_head_node.get_next_node()
        return newArray
  
l = LinkedList(59)
l.insert_beginning(499)
l.insert_beginning(4978)
l.insert_beginning(4910)
l.insert_beginning(500)

print(l.showLinkedList())




