import sys
input = sys.stdin.readline()

N = int(input())
idx = [0] * N
arr = list(map(int,input().split()))
stack=[]

# 6 9 5 7 4
for i in range(N):
    while stack:
        if stack[-1][1] > arr[i]:
            idx[i]=stack[-1][0]+1
            break
        else:
            stack.pop()

    stack.append((i,arr[i]))
print(*idx)