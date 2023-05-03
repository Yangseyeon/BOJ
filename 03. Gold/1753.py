import sys
v, e = map(int, sys.stdin.readline().strip().split())
start_node = int(sys.stdin.readline().strip())
edges = {}
dist = [(10*v + 1) for _ in range(v)]
visit = []
dist[start_node - 1] = 0

for _ in range(e):
    v1, v2, w = map(int, sys.stdin.readline().strip().split())
    if v1 - 1 in edges.keys():
        edges[v1 - 1].append([v2 - 1, w])
    else:
        edges[v1 - 1] = [[v2 - 1, w]]
visit.append(start_node - 1)
for _ in range(v):
    u = visit.index(min(visit))


    for i in range(v):
        if dist[i] < min_dist and visit[i] == False:
            min_dist = dist[i]
            u = i    
    visit[u] = True

    if u not in edges.keys():
        continue
    for l in edges[u]:
        v2 = l[0]
        w = l[1]
        
        if visit[v2] == False and dist[u] + w < dist[v2]:
            dist[v2] = dist[u] + w

for i in dist:
    if i == (10*v + 1):
        print("INF")
        continue
    print(i)


