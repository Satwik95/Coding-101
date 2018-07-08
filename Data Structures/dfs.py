
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
        "f" : ["c"]
        }

V = ['a','b','c','d','e','f']

def dfs_util(u,visited,parent):
    visited[u] = 1
    print(u+"->",end="")
    for v in Graph[u]:
        if v not in visited:
            parent[v]=u
            dfs_util(v,visited,parent)
            
def dfs(src):
    visited = {}
    parent={}
    parent[src]=None
    connected_comp = 1
    dfs_util(src,visited,parent)
    for v in V:
        if v not in visited:
            dfs_util(v,visited,parent)
            connected_comp+=1
    print("Total Connected Comp are:",connected_comp)
    print("Parents",parent)


dfs("a")
