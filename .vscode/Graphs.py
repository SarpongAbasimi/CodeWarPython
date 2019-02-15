"""
Graphs are the perfect data structure for modeling networks, which make them an indispensable piece of your data structure toolkit. 
They're composed of nodes, or vertices, which hold data, and edges, which are a connection between two vertices. 
A single node is a vertex.

Consider a map of the area where you live. As a graph, we could model bus stops as vertices, 
with bus routes between stops functioning as the edges.
What about the internet? Web pages can be vertices, and the hyperlinks which connect them are edges.
Real-world relationships modeled as graphs are numerous, making them an essential concept to master.

#Weighted Graph
We're building a graph of favorite neighborhood destinations (vertices) and routes (edges), but not all edges are equal. 
It takes longer to travel between Gym and Museum than it does to travel between Museum and Bakery.
This is a weighted graph, where edges have a number or cost associated with traveling between the vertices. 
When tallying the cost of a path, we add up the total cost of the edges used.

These costs are essential to algorithms that find the shortest distance between two vertices.

Gym and Library are adjacent, there's one edge between them, 
but there's less total cost to travel from Gym to Bakery to Library (10 vs. 9).

#Directed Graph
Imagine you're a superhero escaping a villain's lair. As you move from perilous room to perilous room, 
the doors close immediately behind you, barring any return.
For this dramatic example, we need a directed graph, where edges restrict the direction of movement between vertices.
We can move from spikes to lasers, but not from lasers to spikes. This differs from earlier examples when every edge was bi-directional.
Note the path spikes to lasers to piranhas to spikes. This path is a cycle, because it ends on the vertex where it began: spikes.

Reviewing Key Terms
Graphs are an essential data structure in computer science for modeling networks. Let's review some key terms:

vertex: A node in a graph.
edge: A connection between two vertices.
adjacent: When an edge exists between vertices.
path: A sequence of one or more edges between vertices.
disconnected: Graph where at least two vertices have no path connecting them.
weighted: Graph where edges have an associated cost.

directed: Graph where travel between vertices can be restricted to a single direction.
cycle: A path which begins and ends at the same vertex.
adjacency matrix: Graph representation where vertices are both the rows and the columns. Each cell represents a possible edge.
adjacency list: Graph representation where each vertex has a list of all the vertices it shares an edge with.

"""
