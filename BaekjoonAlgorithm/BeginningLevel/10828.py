'''
Create a stack process program that processes commands.

info.
push X: integer x into the stack
pop: pop and output the highest integer. If the stack is empty, output -1.
size: output the number of integers
empty: If the stack is empty, output -1 or 1.
top: output the highest integer. If the stack is empty, output -1.
'''

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
