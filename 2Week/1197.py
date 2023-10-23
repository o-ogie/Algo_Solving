import sys

def find_parent(parent, x):
    if parent[x]==x:
        return x
    return find_parent(parent,parent[x])

def union_parent(parent, x, y):
    X = find_parent(parent,x)
    Y = find_parent(parent,y)

    if X==Y:
        return True
    elif X<Y:
        parent[Y] = X
        return False
    else:
        parent[X] = Y
        return False

V, E = map(int,sys.stdin.readline().split())

edges=[]
result = 0
for _ in range(E):
    # A번 B번 가중치 C
    A, B, C = map(int,sys.stdin.readline().split())
    edges.append((A,B,C))

parent = [i for i in range(V+1)]

# edges = sorted(edges, key=lambda x:x[2])
edges.sort(key=lambda x: x[2])
for edge in edges:
    a, b, cost = edge

    if not union_parent(parent,a,b):
        result += cost

print(result)
