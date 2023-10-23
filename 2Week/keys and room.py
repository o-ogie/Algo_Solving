# 호텔 방에 키가 존재한다.
# 1번 방에는 1, 3번 방의 열쇠
# 2번 방에는 0, 1, 3, 5
# 3번 방에는 2, 4
# 4번 방에는 0, 2
# 5번 방에는 없다
# 6번 방에는 없다.
# 1번 방부터 시작한다고 하면 전부다 들어갈 수 있는지 True or False를 반환하라.


# DFS/ stack
# N = int(input())

# graph=[]
# visited=set()
# visited.add(0)
# stack=[0]

# for i in range(N):
#     graph.append(list(map(int,input().split()))) # 방마다 몇 번 방의 열쇠를 갖는지.

# while stack:
#     for key in graph[stack.pop()]:
#         if key not in visited:
#             stack.append(key)
#             visited.add(key)

# if len(visited) == len(graph):
#     print(True)
# else:
#     print(False)


# BFS/ queue
from collections import deque

N = int(input())

que = deque()
que.append(0)
visited = set()
visited.add(0)
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

while que:
    for key in graph[que.popleft()] :
        if key not in visited:
            visited.add(key)
            que.append(key)

if len(visited) == len(graph):
    print(True)
else:
    print(False)