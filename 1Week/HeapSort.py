import sys
N = int(input())
# arr = list(map(int,input().split()))
arr = [int(sys.stdin.readline()) for i in range(N)]

def maxHeap(size):

    for i in range(size//2-1,-1,-1):
        shiftDown(i,size)


    for i in range(1,size):
        arr[0], arr[size-i] = arr[size-i], arr[0]
        shiftDown(0,size-i)



def shiftDown(parentNode, size):
    largeIdx = False
    left= 2*parentNode+1
    right = left+1

    if left <size :
        largeIdx=left

    if right <size and arr[left]<arr[right]:
        largeIdx=right

    if largeIdx and arr[largeIdx] > arr[parentNode]:
        arr[largeIdx], arr[parentNode] = arr[parentNode], arr[largeIdx]
        shiftDown(largeIdx, size)

maxHeap(N)
print(*arr)