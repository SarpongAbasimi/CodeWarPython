""" 
Introduction to Heaps
Heaps are used to maintain a maximum or minimum value in a dataset. Our examples use numbers since this is a straight-forward value, 
but heaps have many practical applications.

Imagine you have a demanding boss (hopefully this is theoretical!). They always want the most important thing done. Of course,
once you finish the most important task, another one takes its place.

You can manage this problem using a priority queue to ensure you're always working on the most pressing assignment and 
heaps are commonly used to create a priority queue.

Heaps tracking the maximum or minimum value are max-heaps or min-heaps. We will focus on min-heaps, 
but the concepts for a max-heap are nearly identical.

Think of the min-heap as a binary tree with two qualities:

The root is the minimum value of the dataset.
Every child's value is greater than its parent.
These two properties are the defining characteristics of the min-heap. 
By maintaining these two properties, we can efficiently retrieve and update the minimum value.

**********************
Heap Representations**
**********************
We can picture min-heaps as binary trees, where each node has at most two children. 
As we add elements to the heap, they're added from left to right until we've filled the entire level.

At the top, we've filled the level containing 12 and 20. 
The next addition comes as the left child of 12, starting a new level in the tree. 
We would continue filling this level from left to right until 20 had its right child filled.

Conceptually, the tree representation is beneficial for understanding. 
Practically, we implement heaps in a sequential data structure like an array or list for efficiency.

Notice how by filling the tree from left to right; we're leaving no gaps in the array. 
The location of each child or parent derives from a formula using the index.

left child: (index * 2) + 1
right child: (index * 2) + 2
parent: (index - 1) / 2 — not used on the root!

**************
Heaping Up ***
**************
# start at the last element of the list
# while there's a parent element available:
# if the parent element is greater:
# swap the elements
# set the target element index to be the parent's index

"""

class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # NEW HELPER!
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS
  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    print("Removing: {0} from {1}".format(min, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
      
  def heapify_down(self):
    idx = 1
    while self.child_present(idx):
      print("Heapifying down!")
      smaller_child_idx = self.get_smaller_child_idx(idx)
      child = self.heap_list[smaller_child_idx]
      parent = self.heap_list[idx]
      if parent > child:
        self.heap_list[idx] = child
        self.heap_list[smaller_child_idx] = parent
      idx = smaller_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))

  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        print("Left child is smaller")
        return self.left_child_idx(idx)
      else:
        print("Right child is smaller")
        return self.right_child_idx(idx)
    
  def heapify_up(self):
    idx = self.count
    while self.parent_idx(idx) > 0:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        tmp = self.heap_list[self.parent_idx(idx)]
        print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")
