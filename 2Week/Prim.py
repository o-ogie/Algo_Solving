import heapq

def prim(graph,start):
    V = len(graph)
    visited = [False] * V
    dist = [float('inf')] * V
    dist[start] = 0
    mst = []
    que = [(dist[start], start)]  # (distance, vertex)

    while que:
        cost, u = heapq.heappop(que)
        if visited[u]:
            continue

        visited[u] = True
        mst.append(u)
        for v, weight in enumerate(graph[u]):
            if weight and not visited[v] and weight < dist[v]:  # weight가 0이 아닌 경우만 고려
                dist[v] = weight
                heapq.heappush(que, (dist[v], v))


    return mst

# 예제 그래프 (인접 행렬)
graph = [
    [0, 1, 4, 0, 0],
    [1, 0, 2, 5, 0],
    [4, 2, 0, 1, 3],
    [0, 5, 1, 0, 2],
    [0, 0, 3, 2, 0]
]

print(prim(graph,2))
