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

"""
