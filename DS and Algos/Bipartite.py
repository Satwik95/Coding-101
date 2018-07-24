def isBipartite(s,graph):
    parent = {s:None}
    level = {s:0}
    frontier = [s]
    color = {}
    for i in range(1,V):
        color[i]=-1
    color[int(s)] = 0
    i=1
    while frontier:
        next = []
        for u in frontier:
            for v in graph[u]:
                if color[int(u)]==color[int(v)]:
                    return False
                if v not in level:
                    color[int(v)]=color[int(u)]^1
                    level[v]=i
                    parent[v]=u
                    next.append(v)
        frontier = next
        i+=1
    return True

graph = { "1" : ["2","3"],
          "2" : ["3","1","4"],
          "3" : ["1","4"],
          "4" : ["2","3"]
        }
V=5
print(isBipartite("1",graph))
