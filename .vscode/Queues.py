"""
A queue is a data structure which contains an ordered set of data.

Queues provide three methods for interaction:

Enqueue - adds data to the "back" or end of the queue
Dequeue - provides and removes data from the "front" or beginning of the queue
Peek - reveals data from the "front" of the queue without removing it
This data structure mimics a physical queue of objects like a line of people buying movie tickets. 
Each person has a name (the data). The first person to enqueue, or get into line, is both at the front and back of the line. 
As each new person enqueues, they become the new back of the line.

When the cashier serves someone, they begin at the front of the line (or people would get very mad!).
Each person served is dequeued from the front of the line, they purchase a ticket and leave.

If they just want to know who is next in line, they can peek and get their name without removing them from the queue.

The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure.

Queues:

Contain data nodes
Support three main operations:
Enqueue adds data to the back of the queue
Dequeue removes and provides data from the front of the queue
Peek provides data on the front of the queue
Can be implemented using a linked list or array
Bounded queues have a limited size.
Enqueueing onto a full queue causes a queue overflow
Queues process data First In, First Out (FIFO)

#Python Implemetation - Code Academy.

Queues Python Size
Bounded queues require limits on the number of nodes that can be contained, while other queues don't. 
To account for this, we will need to make some modifications to our Queue class so that we can keep track of and limit size where needed.

We'll be adding two new properties to help us out here:

A size property to keep track of the queue's current size
A max_size property that bounded queues can utilize to limit the total node count
In addition, we will add three new methods:

get_size() will return the value of the size property
has_space() will return True if the queue has space for another node
is_empty() will return true if the size is 0

Queues Python Enqueue
"Enqueue" is a fancy way of saying "add to a queue," and that is exactly what we're doing with the enqueue() method.

There are three scenarios that we are concerned with when adding a node to the queue:

The queue is empty, so the node we're adding is both the head and tail of the queue
The queue has at least one other node, so the added node becomes the new tail
The queue is full, so the node will not get added because we don't want queue "overflow"
Let's put this into action by building out an enqueue() method for Queue.


We can add items to the tail of our queue, but we remove them from the head using a method known as dequeue(), 
which is another way to say "remove from a queue". 
Like enqueue(), we care about the size of the queue — but in the other direction, so that we prevent queue "underflow". 
After all, you don't want to remove something that isn't there!

As with peek(), our dequeue() method should return the value of the head. Unlike, peek(), 
dequeue() will also remove the current head and replace it with the following node.

For dequeue, there are three scenarios that we will take into account:

The queue is empty, so we cannot remove or return any nodes lest we run into queue "underflow"
The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue's head and tail to None
The queue has more than one node, and we just remove the head node and reset the head to the following node

"""






