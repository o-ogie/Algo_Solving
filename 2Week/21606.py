N = int(input())

place = [0] + list(map(int,input()))
graph=[[]for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0

def DFS(start):
    global cnt
    stack=[start]
    visited=set()
    while stack:
        value = stack.pop()
        if value in visited:
            continue
        visited.add(value)

        for node in graph[value]:

            if node not in visited:
                if place[node]:
                    # print(value, node, place[node])
                    cnt += 1
                    visited.add(node)
                    continue
                stack.append(node)

for i in place:
    if i == 1:
        DFS(i)

print(cnt)
