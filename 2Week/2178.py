from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(n, m, maze):
    queue = deque([(1, 1)])
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[1][1] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m and maze[nx][ny] == 1 and not visited[nx][ny]:
                maze[nx][ny] = maze[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return maze[n][m]

n, m = map(int, input().split())
maze = [[]]
for _ in range(n):
    row = [0] + list(map(int, list(input())))
    maze.append(row)
print(maze)
print(bfs(n, m, maze))
