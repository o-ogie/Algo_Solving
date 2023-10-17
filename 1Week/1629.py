import sys

A, B, C = map(int, sys.stdin.readline().split())


def mul(A, B, C) :
    if B==0:
        return 1

    elif B%2==0 :
        result = mul(A,B//2,C)
        return result * result % C
    else:
        result = mul(A,B//2,C)
        return result * result * A % C

print(mul(A,B,C))

# 모듈로 연산 분배 법칙.