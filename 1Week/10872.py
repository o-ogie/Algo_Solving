# def factorial(N) :
#     if N<=1:
#         return 1
#     return N * factorial(N-1)

# print(factorial(int(input())))


def factorial(N):
    DP=[1,1]+[0] * (N-1)
    for i in range(2,N+1):
        DP[i] = DP[i-1]*i
    return DP[-1]

print(factorial(int(input())))
