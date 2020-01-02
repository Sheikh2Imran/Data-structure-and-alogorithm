"""
Author: Md Imran Sheikh
Jr. Software Enginer
Circle Fintech Ltd.
"""
class Graph:
    def __init__(self, total_node):
        self.total_node=total_node
        self.adjecency_matrix = [[-1]*total_node for i in range(total_node)]
        self.nodes = {}
        self.node_list = [0]*total_node
        
    def set_node(self, node, id):
        self.nodes[id]=node
        self.node_list[node]=id

    def set_edge(self, start, end, weight=0):
        u = self.nodes[start]
        v = self.nodes[end]
        self.adjecency_matrix[u][v] = weight
        self.adjecency_matrix[v][u] = weight

    def get_ajancency_matrix(self):
        return self.adjecency_matrix

    
    def get_node_list(self):
        return self.node_list
        

graph = Graph(total_node=6)
graph.set_node(0, 'a')
graph.set_node(1, 'b')
graph.set_node(2, 'c')
graph.set_node(3, 'd')
graph.set_node(4, 'e')
graph.set_node(5, 'f')
graph.set_edge('a', 'b', 3)
graph.set_edge('b', 'c', 2)
graph.set_edge('c', 'd', 1)
graph.set_edge('d', 'e', 7)
graph.set_edge('e', 'f', 5)
print(graph.get_ajancency_matrix())
