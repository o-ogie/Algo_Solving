N = int(input())
graph = {}

for _ in range(N):
    root, left, right= map(str,input().split())
    graph[root] = [left,right]

def prefix(root):
    if root != '.':
        print(root, end="")
        prefix(graph[root][0])
        prefix(graph[root][1])

def infix(root):
    if root != '.':
        infix(graph[root][0])
        print(root, end="")
        infix(graph[root][1])

def postfix(root):
    if root != '.':
        postfix(graph[root][0])
        postfix(graph[root][1])
        print(root, end="")


prefix("A")
print()
infix("A")
print()
postfix("A")