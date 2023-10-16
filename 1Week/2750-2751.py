import sys

arr = []
for _ in range(int(input())):
    arr.append(int(sys.stdin.readline()))

# 1,4,2,3,5
# arr.sort()

## 버블 정렬
def bubble_sort(arr:list):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


## 선택 정렬
# def selection_sort(arr:list) :
#     for i in range(len(arr)) :
#         min_index = i
#         for  j in range(i,len(arr)):
#             if arr[min_index] > arr[j]:
#                 min_index=j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


## 삽입 정렬
# def insertion_sort(arr:list):
#     for i in range(1,len(arr)):
#         k = i
#         temp = arr[k]

#         while k>0 and arr[k-1]>temp:
#             arr[k] = arr[k-1]
#             k -= 1
#         arr[k] = temp
#     return arr

# print(*insertion_sort(arr))


## 퀵 정렬
# def quick_sort(arr:list) :
#     if len(arr)<=1:
#         return arr
#     pivot = arr[0]
#     lowArr, equel, highArr = [i for i in arr[1:] if pivot>i], [pivot]+[ i for i in arr[1:] if i==pivot], [i for i in arr[1:] if pivot<i]
#     return quick_sort(lowArr) + equel + quick_sort(highArr)

# print(*quick_sort(arr))

# 머지 정렬
def merge_sort(arr:list) :
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left:list, right:list):
    sorted_list = []
    i,k = 0,0
    while i<len(left) and k < len(right):
        if left[i] < right[k]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[k])
            k +=1
    while i<len(left):
        sorted_list.append(left[i])
        i +=1
    while k<len(right):
        sorted_list.append(right[k])
        k+=1
    return sorted_list
print(*merge_sort(arr))

## 힙 정렬


##기수 정렬


## 계수 정렬