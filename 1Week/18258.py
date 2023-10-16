import sys

queue = []
index = 0
for _ in range(int(sys.stdin.readline())):
    state = sys.stdin.readline().split()

    if state[0]=="push":
        queue.append(state[1])
    elif state[0]=="pop":
        if len(queue)>index:
            print(queue[index])
            queue[index]=0
            index+=1
        else:
            print(-1)
    elif state[0] == "size":
        print(len(queue)-index)
    elif state[0] == "empty":
        if len(queue)==index:
            print(1)
        else:
            print(0)
    elif state[0] == "front":
        if len(queue)>index:
            print(queue[index])
        else:
            print(-1)
    elif state[0] == "back":
        if len(queue)>index:
            print(queue[-1])
        else:
            print(-1)
        