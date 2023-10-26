from queue import Queue
N, M, V = map(int,input().split())

graph = [[]for _ in range(N+1)]

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

for _ in range(1,M+1):
    start, end = map(int,input().split())
    graph[start].append(end)
    if start not in graph[end]:
        graph[end].append(start)

graph = [sorted(row) for row in graph]

# print(graph)
# def DFS(start):
#     stack=[start]
#     visited = set()
#     result = []
#     while stack:
#         value = stack.pop()
#         if value in visited:
#             continue
#         result.append(value)
#         visited.add(value)
#         for neighbor in sorted(graph[value], reverse=True):  # graph[value] 
#             if not neighbor in visited:
#                 stack.append(neighbor)
#     print(" ".join(map(str,result)))
def DFS(start):
    stack = [start]
    visited = set()
    visited.add(start)
    result = []
    while stack:
        value = stack.pop()
        result.append(value)
        for neighbor in sorted(graph[value], reverse=True):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    print(*result)

# stack=[]
# visited=[False]*(N+1)
stack=[]
visited=[False]*(N+1)


# def DFS(start) :
#     print(start, end=" ")
#     stack.append(start)
#     visited[start] = True

#     while stack:
#         value = stack.pop()

#         for neighbor in graph[value]:
#             if not visited[neighbor]:
#                 DFS(neighbor)


def BFS(start):
    que = Queue()
    que.put(start)
    visited = [start]
    while not que.empty():
        value = que.get()
        for neighbor in graph[value]:
            if neighbor not in visited:
                que.put(neighbor)
                visited.append(neighbor)

    print(*visited)

DFS(V)
BFS(V)