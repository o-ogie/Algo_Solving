graph=[[]for _ in range(int(input())+1)]
for node in range(int(input())):
    v,e = map(int,input().split())
    graph[v].append(e)
    if v not in graph[e]:
        graph[e].append(v)

def virus(start):
    stack=[start]
    visited=set()

    while stack:
        value=stack.pop()

        if value in visited:
            continue
        visited.add(value)

        for neighbor in graph[value]:
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited)-1

print(virus(1))
