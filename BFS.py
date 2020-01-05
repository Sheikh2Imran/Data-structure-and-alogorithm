from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v) 

    def BFS(self, s):
        visited = [False]*len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print (s, end = " ") 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 

g.BFS(2)

"""
Applications of Breadth First Traversal:
1. Peer to Peer Networks like bitTorrent.
2. Crawlers in Search Engines.
3. Social Networking Websites.
4. Breadth First Search is used to find all neighboring locations.
5.  Broadcasting in Network.
6. copying garbage collection using Cheney’s algorithm.
7. We can either use Breadth First or Depth First Traversal to find if there is a path between two vertices.
"""
