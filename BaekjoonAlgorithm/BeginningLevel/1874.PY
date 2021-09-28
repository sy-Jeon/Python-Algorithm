'''
Question:
By putting numbers from 1 to n into the stack and pulling them out, we can create a sequence.
In this case, let's say that the order of pushing the stack must be kept in ascending order.
Given an arbitrary sequence, we can use the stack to figure out in which order we should perform push and pop operations.
Write a program that calculates this.

Info.
The first line is given n (1 n n 100 100,000).
From the second line, n lines are given in order with integers of 1 or more and n or less that make up the sequence.
Of course, the same integer does not come out twice.

Outputs one operation per line required to create an input sequence.
The push operation is expressed as + and the pop operation is expressed as -.
If impossible, output NO.
'''

stack = []
result = []
count = 1
flag = 1

n = int(input())
for i in range(n):
    command = int(input())
    
    while count <= command:
        stack.append(count)
        result.append("+")
        count += 1
    
    if stack[-1] == command:
        stack.pop()
        result.append("-")
    else:
        print('NO')
        flag = 0
        break

if flag == 1:
    for i in range(len(result)):
       print(result[i])