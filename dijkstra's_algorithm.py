from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertex):
        self.vertexs = num_of_vertex
        self.edges = [[-1 for i in range(num_of_vertex)] for i in range(num_of_vertex)]
        self.visited = []
        
    def add_edge(self, vertex1, vertex2, weight):
        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight
        
    def dijkstra(self, start_vertex):
        D = {vertex: float('inf') for vertex in range(self.vertexs)}
        D[start_vertex] = 0
        pq = PriorityQueue()
        pq.put((0, start_vertex))
        
        while not pq.empty():
            (dist, u) = pq.get()
            self.visited.append(u)
            
            for v in range(self.vertexs):
                if self.edges[u][v] != -1:
                    distance = self.edges[u][v]
                    if v not in self.visited:
                        old_cost = D[v]
                        new_cost = D[u] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, v))
                            D[v] = new_cost

        return D
        
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 2)
    
    D = g.dijkstra(0)
    
    print(D)
