from collections import deque

# 노드 N개, 간선 M개
N, M = map(int,input().split())

indegree = [0]*(N+1)

graph = [[] for _ in range(N+1)]

que = deque()
result = []

for _ in range(M):
    prev, next = map(int,input().split())
    graph[prev].append(next)
    indegree[next] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    print(que)
    value = que.popleft()
    print(value)
    result.append(value)
    for i in graph[value]:
        indegree[i] -=1
        if indegree[i] == 0:
            que.append(i)

print(result)