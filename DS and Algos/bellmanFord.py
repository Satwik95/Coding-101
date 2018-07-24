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

    def bellmanFord(self,src):
        V = len(self.vertices)
        dist = [float("inf")]*(V+1)
        dist[src]=0
        #relax for |vertices|-1  times
        for i in range(V-1):
            for u,v,w in self.edge_list:
                if dist[u]!=float("inf") and dist[v]>dist[u]+w:
                    dist[v]= dist[u]+ w
        for u,v,w in self.edge_list:
            if dist[u]!=float("inf") and dist[v]>dist[u]+w:
                print("Negative cycle exists!")
                return
        print(src,  dist[1:])
        return
                
if __name__ == '__main__':

    vertices = [1,2,3]
    g = Graph(vertices,False) 
    g.add_edge(1,2,1)
    g.add_edge(2,3,2)
    g.add_edge(3,1,-4)
    g.make_graph()
    g.bellmanFord(1)
