def isPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N%i==0:
            return False
    return True


for _ in range(int(input())):
    N = int(input())
    A, B = N//2, N//2
    for _ in range(N//2):
        if isPrime(A) and isPrime(B):
            print(A, B)
            break
        else:
            A-=1
            B+=1