def flatten(g):
    flattened_list = [y for x in g for y in x]
    return flattened_list

def bfs(s,graph):
    parent = {s:None}
    level = {s:0}
    frontier = [s]
    i=1
    while frontier:
        next = []
        for u in frontier:
            for v in graph[u]:
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    next.append(v)
        frontier = next
        i+=1

    print(parent)
    print(level)

graph = { "a" : ["c"],
          "b" : ["c"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c"]
        }

bfs("a",graph)
