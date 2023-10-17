import sys

def paper(y, x, N):
    allPass= True
    if N == 1 :
        color[arr[y][x]]+=1
        return
    mid = N//2
    pivot = arr[y][x]
    for i in range(y, y+N):
        if pivot^1 in arr[i][x:x+N]:
            allPass = False

    if allPass:
        color[arr[y][x]]+= 1
        return
    else :
        paper(y,x,mid)
        paper(y,x+mid,mid)
        paper(y+mid,x,mid)
        paper(y+mid, x+mid,mid)  


N = int(input())

arr = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
color = [0,0]

paper(0,0,N)

for i in color:
    print(i)


'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 1 0 1 1 0 0
0 0 0 1 1 1 0 0
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
'''
