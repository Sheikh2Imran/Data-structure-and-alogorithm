# pseudocode of Breadth First Search
1. create a queue Q
2. Mark source as visited and enqueue to queue Q.
3. while Q is not empty:
    1. Remove the head u from Q
    2. Mark as visited and enqueue the neighbors of u.

# if this is the graph    
    1
   /  \
  2    4
 / \    \
3   9    7
    
# And i will save this graph in adjacency list, then i looks like below.
{
    1: [2, 4],
    2: [3, 9],
    4: [7],
}

# I am going to use adjancency list. Because i can set the required space at run time.
# If there are n nodes and if i use adjancency matrix then the space complexity will be n * n.

# Also Time complexity is lower than adjancency matrix. When i have to search the adjacency node \
# of a node then it helps beacuse i don't need to search the hole thing. Then time complexity is n.
 

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = [False]*len(self.graph)

    def add_edge(self, u, v):
        self.graph[u].append(v) 

    def BFS(self, source, desired_num):
        self.visited.append(source)
        queue = []
        queue.append(source)
        level = {}
        level[source] = 0

        while queue:
            u = queue.pop(0)
            if u == desired_num:
                print("Level: ", level[u])

            for v in self.graph[u]:
                if not v in self.visited:
                    queue.append(v)
                    self.visited.append(v)
                    level[v] = level[u] + 1

g = Graph()

g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(2, 6)
g.add_edge(4, 7)
g.add_edge(3, 7)
g.add_edge(3, 8)
g.add_edge(6, 10)
g.add_edge(7, 9)
g.add_edge(8, 5)
g.add_edge(9, 10)

g.BFS(1, 10)


"""
Applications of Breadth First Traversal:
1. Peer to Peer Networks like bitTorrent.
2. Social Networking Websites.
3. Breadth First Search is used to find all neighboring locations.
4. We can either use Breadth First or Depth First Traversal to find if there is a path between two vertices.
5. Broadcasting in Network.
"""
