# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.


# 1. list 메서드 사용
# arr=[]
# for i in range(9):
#     arr.append(int(input()))
# max = max(arr)
# print(max)
# print(arr.index(max)+1)

# 2. 알고리즘 구현
arr=[]
max=0
idx=0
for i in range(9):
    arr.append(int(input()))

for i in arr:
    if i > max:
        max=i
print(max)

for i in range(len(arr)):
    if max==arr[i]:
        idx=i+1
print(idx)
