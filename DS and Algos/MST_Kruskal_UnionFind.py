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

    def util_sorted(self,x):
        return x[2]

    def find(self,parent,i):
        if parent[i]==i:
            return i
        else:
            return self.find(parent,parent[i])#recursively find the base parent
            
    def union(self,parent,u,v):
        p1 = self.find(parent,u)
        p2 = self.find(parent,v)
        parent[p2] = p1
        
    def isCycle(self):
        parent=[-1]*len(self.vertices)
        for u,v,w in self.edge_list:
            p1 = self.find(parent,u)
            p2 = self.find(parent,v)
            if p1==p2:
                return True
            self.union(parent,u,v)
            
    def Kruskal_MST(self):
        #starting from 1st node, not including 0 as a node, will be
        # V if o is included
        parent=[i for i in range(len(self.vertices)+1)]
        sorted_edges = sorted(self.edge_list,key = self.util_sorted)
        mst = []
        for i in range(len(self.vertices)-1):
            for u,v,w in sorted_edges:
                p1 = self.find(parent,u)
                p2 = self.find(parent,v)
                if p1!=p2:
                    mst.append([u,v,w])
                    #self.union(parent,u,v)
                        
        print(parent,mst)
                
if __name__ == '__main__':

    vertices = [1,2,3]
    g = Graph(vertices,False) 
    g.add_edge(1,2,1)
    g.add_edge(2,3,2)
    g.add_edge(3,1,4)
    g.make_graph()
    g.Kruskal_MST()
