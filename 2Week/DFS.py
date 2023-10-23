def dfs(graph, node, visited):
    if not visited[node]:
        print(node,end=",")  # 노드 출력
        visited[node] = True  # 노드 방문 표시
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited)  # 재귀적으로 이웃 노드 탐색

# 예제 그래프
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}



visited = [False] * len(graph)

# 0번 노드에서 시작하여 DFS 수행
dfs(graph, 0, visited)

print()


def dfs_iterative(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    visited[start] = True
    stack = [start]
    
    while stack:
        node = stack.pop()
        print(node, end ="")
        for neighbor in range(num_nodes):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                # print(node, neighbor, graph[node][neighbor], end="/")
                stack.append(neighbor)
                visited[neighbor] =True

# 인접 행렬로 표현된 그래프
graph = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

# 0번 노드에서 시작하여 DFS 수행
dfs_iterative(graph, 0)
print()

graph = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,0,1],
    [0,1,0,0,0,0],
    [0,1,0,0,0,1],
    [0,0,1,0,1,0]
]

visited = [False] * len(graph)

def DFS(start):
    visited[start] = True
    print(start,end="")
    for neighbor in range(len(graph)):
        if graph[start][neighbor] == 1 and not visited[neighbor]:
            DFS(neighbor)

DFS(0)

