import sys

N = int(sys.stdin.readline())

AN = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

AN.sort()

for num in arr :
    lt, rt = 0, N-1
    isExist = False

    while lt<=rt:
        mid = (lt+rt)//2

        if num == AN[mid]:
            isExist=True
            break
        elif num>AN[mid]:
            lt=mid+1
        else:
            rt=mid-1


    print(isExist*1)


# import sys

# N = int(sys.stdin.readline())

# AN = set(map(int,sys.stdin.readline().split()))

# M = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))

# for i in arr:
#     print((i in AN)*1)