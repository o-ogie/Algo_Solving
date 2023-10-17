import sys

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
trees.sort()

start = 1
end = max(trees)

def search(trees:list):
    global start, end
    while start <= end:
        mid = (start+end)//2
        height=0
        for tree in trees:
            if tree>mid:
                height+=tree-mid

        if height>=M:
            start=mid+1
        elif height<M:
            end=mid-1

    print(end)


search(trees)
