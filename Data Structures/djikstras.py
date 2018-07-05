from collections import defaultdict
import collections
import sys
import heapq

class Graph:
    def __init__(self,vertices,isUndirected=True):
        self.vertices = vertices
        self.edge_list = []
        self.isUndirected = isUndirected
        self.adj_list = defaultdict(list)
        self.weight_list = {}
        self.adj_matrix = [[0 for x in range(len(vertices)+1)] for y in range(len(vertices)+1)]

    def add_edge(self,u,v,w=None):
        self.edge_list.append([u,v,w if w else 1])
        if self.isUndirected:
            self.edge_list.append([v,u,w if w else 1])

    def make_graph(self):
        for u,v,w in self.edge_list:
            self.adj_list[u].append(v)
            self.weight_list[u,v]=w
            self.adj_matrix[u][v] = w

    def djikstras(self,src,graph,weights):
        parent = {src:None}
        dist = {}
        #setting all distance as inf
        for v in vertices:
            dist[v] = sys.maxsize
        dist[src] = 0
        #to find out the node with the min distance, pick the first element, using heap
        frontier = []
        heapq.heappush(frontier,(0,src))
        level = {src:0}
        i=1
        while frontier:
            next = []
            #find the pair at front, always taking the item with the min distance
            for w,u in frontier:
                parent_dist = w
                #iterate over the neighbours of the cur node
                for v in graph[u]:
                    #print(u,v)
                    cur_dist = parent_dist + weights[(u,v)]
                    #print(cur_dist)
                    if cur_dist< dist[v]:
                        dist[v]=cur_dist
                        parent[v]=u
                        level[v]=i
                        heapq.heappush(next,(dist[v],v))
            frontier = next
            i+=1
        print(dist)
                
if __name__ == '__main__':

    vertices = [1,2,3,4]
    g = Graph(vertices) 
    g.add_edge(1,2,1)
    g.add_edge(1,3,4)
    g.add_edge(2,3,1)
    g.add_edge(3,4,2)
    g.add_edge(1,4,7)
    g.make_graph()
    g.djikstras(1,g.adj_list,g.weight_list)

