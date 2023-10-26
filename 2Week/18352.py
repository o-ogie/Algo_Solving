from collections import deque

N, M, K, X= map(int,input().split())
graph=[[]for _ in range(M+1)]
visited=set()
distance=[0] * N + 1
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
  

def BFS(start,count):
    que=deque([start])
    visited=set()
    answer=[]
    while que:
        value=que.popleft()


BFS(X,0)
