import sys

stack=[]

for _ in range(int(input())):
    state= sys.stdin.readline().split()
    if state[0] == "push":
        stack.append(state[1])
    elif state[0] == "pop":
        if stack:
            print(stack.pop())
        else :
            print(-1)
    elif state[0] == "size":
        print(len(stack))
    elif state[0] == "empty":
        print((not len(stack)) * 1)
    elif state[0] == "top":
        if stack :
            print(stack[-1])
        else :
            print(-1)