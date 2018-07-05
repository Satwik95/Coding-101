from collections import defaultdict

class Graph:
    def __init__(self,vertices,isUndirected=True):
        self.vertices = vertices
        self.edge_list = []
        self.isUndirected = isUndirected
        self.adj_list = defaultdict(list)
        self.adj_matrix = [[0 for x in range(len(vertices)+1)] for y in range(len(vertices)+1)]

    def add_edge(self,u,v,w=None):
        self.edge_list.append([u,v,w if w else 1])
        if self.isUndirected:
            self.edge_list.append([v,u,w if w else 1])

    def make_graph(self):
        for u,v,w in self.edge_list:
            self.adj_list[u].append([v,w])
            self.adj_matrix[u][v] = w
                
if __name__ == '__main__':

    vertices = [1,2,3,4]
    g = Graph(vertices) 
    g.add_edge(1,2,1)
    g.add_edge(1,3,4)
    g.add_edge(2,3,1)
    g.add_edge(3,4,2)
    g.add_edge(1,4,7)
    g.make_graph()

