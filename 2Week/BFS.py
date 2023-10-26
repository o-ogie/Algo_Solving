from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# 예제 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 'A' 노드에서 시작하여 BFS 수행
bfs(graph, 'A')


from collections import deque

def bfs(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes  # 노드 방문 여부를 저장하는 배열
    queue = deque([start])  # 큐를 사용하여 탐색 순서 관리
    visited[start] = True  # 시작 노드를 방문한 것으로 표시

    while queue:
        node = queue.popleft()  # 큐에서 노드를 꺼내옴
        print(node)  # 노드 출력

        for neighbor in range(num_nodes):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)  # 인접한 노드를 큐에 추가
                visited[neighbor] = True  # 인접한 노드를 방문한 것으로 표시

# 인접 행렬로 표현된 그래프
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

# 0번 노드에서 시작하여 BFS 수행
bfs(graph, 0)


from queue import Queue

def bfs(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    q = Queue()

    q.put(start)
    visited[start] = True

    while not q.empty():
        node = q.get()
        print(node)

        for neighbor in range(num_nodes):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                q.put(neighbor)
                visited[neighbor] = True

# 인접 행렬로 표현된 그래프
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

# 0번 노드에서 시작하여 BFS 수행
bfs(graph, 0)



graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

def bfs(graph, start):
    que = Queue([start])
    visited = [False] * len(graph)

    while que:
        node = que.get()

        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1 and not visited[neighbor] :
                que.put(neighbor)
                visited[neighbor] = True

graph = {
    1: [2, 3, 4],
    2: [1, 4],
    3: [1, 4, 5],
    4: [1, 2, 3, 5],
    5: [3, 4]
}

def DFS(start):
    stack=[start]
    visited=[]

    while stack:
        value=stack.pop()

        if value in visited:
            continue
        visited.append(value)

        for node in sorted(graph[value],reverse=True):
            if node not in visited:
                stack.append(node)

    print(*visited)

def BFS(start):
    que=deque([start])
    visited=set()

    while que:
        value = que.popleft()
        # if value in visited:
        #     continue

        for node in graph[value]:
            if node not in visited:
                que.append(node)
                visited.add(node)
    print(*visited)

DFS(1)
BFS(1)