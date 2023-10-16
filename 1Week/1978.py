# count = 0
# input()

# arr = list(map(int,input().split()))
# for i in arr:
#     for j in range(2,i+1):
#         if i%j==0:
#             if i==j:
#                 count+=1
#             break

# print(count)


# 제곱근까지의 수로 나누어지는지 구하여 소수 구하기.
# count = 0
# N= input()

# arr = list(map(int,input().split()))

# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# for i in arr:
#     if isPrime(i):
#         count+=1
# print(count)

# 에라토스테네스의 체

def primeList(N):
    isPrime=[False, False] + [True]*(N+1)

    for i in range(2, int(N**0.5)+1):
        if isPrime[i]:
            for i in range(2*i,N,i):
                isPrime[i]=False

    return [i for i in range(N) if isPrime[i]==True]

print(primeList(10))

def isPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N%i==0:
            return False
    return True
