from collections import defaultdict
import heapq
import sys
class Graph:
    def __init__(self,vertices,isUndirected=True):
        self.vertices = vertices
        self.edge_list = []
        self.adj_list = defaultdict(list)
        self.isUndirected = isUndirected

    def add_edge(self,u,v,w=None):
        self.edge_list.append([u,v,w])

    def make_graph(self):
        for u,v,w in self.edge_list:
            self.adj_list[u].append([v,w if w else 1])
            if self.isUndirected:
                self.adj_list[v].append([u,w if w else 1])
                
    def BFS(self,s):
        parent = defaultdict(list)
        parent[s].append(None)
        level = defaultdict(list)
        i=1
        level[s].append(0)
        Frontier = []
        Frontier.append(s)
        while Frontier:
            next = []
            for u in Frontier:
                for v,w in self.adj_list[u]:
                    if v not in level:
                        level[v]= i
                        parent[v]=u
                        next.append(v)
            Frontier = next
            i+=1
        return parent

    def bfs_path(self,path,s,d):
        temp=d
        while temp!=s:
            print(temp,end="<-")
            temp = path[temp]
        print(s)

    def djikstras(self,s):
        parent = defaultdict(list)
        level = defaultdict(list)
        dist = {}
        for v in self.vertices:
            dist[v] = sys.maxsize
        dist[s] = 0
        level[s].append(0)
        parent[s].append(None)
        Frontier = []
        heapq.heappush(Frontier,(0,s))
        i=1
        while Frontier:
            next = []
            for parent_cost,u in Frontier:
                for v,w in self.adj_list[u]:
                    cur_cost = int(parent_cost) + int(w)
                    if cur_cost < int(dist[v]):
                        dist[v]=cur_cost
                        parent[v]=u
                        level[v]=i
                        heapq.heappush(next,(dist[v],v))
            Frontier = next
            i+=1
        print(dist)

    def DFS_util(self,visited,s):
        print(s,end="->")
        visited.append(s)
        for v,w in self.adj_list[s]:
            if v not in visited:
                self.DFS_util(visited,v)
                
    def dfs(self,s):
        visited = []
        self.DFS_util(visited,s)
        print("end")
                
if __name__=="__main__":
    vertices = [1,2,3,4,5]
    g = Graph(vertices)
    g.add_edge(1,2,3)
    g.add_edge(1,5,5)
    g.add_edge(2,3,1)
    g.add_edge(2,4,2)
    g.add_edge(5,4,3)
    g.make_graph()
    path = g.BFS(1)
    source=1
    dest=4
    g.bfs_path(path,source,dest)
    g.djikstras(1)
    g.dfs(1)
                
        
