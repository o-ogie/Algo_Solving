for i in range(int(input())):
    roop, string = input().split()
    for j in string:
        print(j*int(roop), end="")
    print("")