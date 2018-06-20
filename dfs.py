
parent = {}
back_edge = {}
"""Graph =     { "a" : ["c"],
          "b" : ["c"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c"],
          "f" : []
        }
"""
Graph =     { "a" : ["c"],
            "b" : ["c"],
          "c" : ["e", "d"],
          "e" : ["b"],
          "d" : [],
        "f" : ['c']
        }

V = ['a','b','c','d','e','f']

def dfs_visit(s,G):
    visited = []
    for v in G:
        if v not in parent:
            parent[v] = s
            visited.append(v)
            print(s+"-->"+v)
            dfs_visit(v,Graph[v])
        if v in visited:
            #print(back_edge)
            back_edge[v] = s


def DFS(V,Graph):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            dfs_visit(s,Graph[s])
            
x = DFS(V,Graph)
print(back_edge)
