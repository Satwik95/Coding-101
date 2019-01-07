"""Graph =     { "a" : ["c"],
          "b" : ["c"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c"],
          "f" : []"""
        
Graph =     { "a" : ["c"],
            "b" : ["c"],
          "c" : ["e", "d"],
          "e" : [],
          "d" : [],
        "f" : ["c"]
        }

V = ['a','b','c','d','e','f']
top_sort = []
flag = 0
def dfs_util(u,visited,parent):
    visited[u] = 1
    print(u+"->",end="")
    for v in Graph[u]:
        if v not in visited:
            parent[v]=u
            dfs_util(v,visited,parent)
            #at this point when we are returning from v, 
            #that means all the nodes dependent on v have been visited
            #do top sort when callinf dfs from one source
            #top_sort.insert(0,v)
        elif v in visited and v!=parent[u]:
            global flag
            flag=1
            #print("For u =",u," and v =",v,"Cycle Exists")
            
            
def dfs(src,parent):
    visited = {}
    connected_comp = 1
    return dfs_util(src,visited,parent)
    
    """top_sort.insert(0,src)
    for v in V:
        #print(v)
        if v not in visited:
            top_sort.insert(0,v)
            x = dfs_util(v,visited)
            if x==False:
                print("Cycle Exists")
            connected_comp+=1
    #use this only when working on undirected graphs
    print("Total Connected Comp are:",connected_comp) 
    #print("Parents",parent)"""
x = []    
for v in V:
    parent = {}
    parent[v]=None
    x.append(dfs(v,parent))

if flag==1:
    print("Cycle exists")
else:
    print("No cycle")
    
print("The topological sort is:",end=" ")
for t in top_sort:
   print(t,end="->")
print("Finish")
