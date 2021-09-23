import sys

n = int(input())
stack = []

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0].find("push") == 0:
        stack.append(s[1])
    elif s[0] == "pop":
        if stack != []:
            print(stack.pop())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(stack))
    elif s[0] == "empty":
        if stack != []:
            print(0)
        else:
            print(1)
    elif s[0] == "top":
        if stack != []:
            print(stack[-1])
        else:
            print(-1)
