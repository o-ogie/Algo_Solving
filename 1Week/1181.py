

# ################ 구현 #####################
# arr = []
# for _ in range(int(input())):
#     arr.append(input())
# # 중복 값 제거
# del_list = []
# for i in range(len(arr)):
#     for j in range(1+i,len(arr)):
#         if arr[i] == arr[j]:
#             print(i)
#             del_list.append(i)

# for i in del_list[::-1]:
#     del arr[i]

# # 동일 글자 수 사전 순 정렬
# for i in range(len(arr)) :
#     for j in range(i+1,len(arr)):
#         if arr[i]>arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]


# # 글자 순 정렬
# for i in range(1, len(arr)) :
#     for j in range(len(arr)-i):
#         if len(arr[j]) > len(arr[j+1]):
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#############################################




# 메서드 사용
arr = list(set(input() for _ in range(int(input()))))
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)