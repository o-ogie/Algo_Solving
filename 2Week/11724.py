# import sys

# N, M = map(int, sys.stdin.readline().split())
# graph = [ [] for _ in range(N + 1) ]
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x].append(y)
#     graph[y].append(x)

# def dfs(start):
#     stack = [start]
#     while stack:
#         value = stack.pop()
#         if value in visited:
#             continue
#         visited.add(value)
#         for neighbor in graph[value]:
#             if neighbor not in visited:
#                 stack.append(neighbor)

                

# conn = 0
# visited = set()

# for i in range(1, N + 1):
#     if i not in visited:
#         dfs(i)
#         conn += 1

# print(conn)

N, M = map(int, input().split())

graph = [ [] for _ in range(N + 1) ]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, visited):
    stack = [start]

    while stack:
        value = stack.pop()
        if value in visited:
            continue
        visited.add(value)
        for neighbor in graph[value]:
            if neighbor not in visited:
                stack.append(neighbor)

conn = 0
visited = set()

for i in range(1, N + 1):
    if i not in visited:
        dfs(i, visited)
        conn += 1

print(conn)
