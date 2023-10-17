arr = []
for _ in range(9):
    arr.append(int(input()))


def friends(arr:list) :
    for i in range(len(arr)-1):
        for k in range(i+1,len(arr)):
            other1 = arr[i]
            other2 = arr[k]
            if sum(arr)-other1-other2 == 100:
                arr.remove(other1)
                arr.remove(other2)
                return arr

for i in sorted(friends(arr)):
    print(i)


