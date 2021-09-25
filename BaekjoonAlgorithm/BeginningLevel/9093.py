'''
Question: Reverse the words.

Info.
t is the number of inputs.
command is word.
'''

import sys

t = int(input())

for i in range(t):
    command = sys.stdin.readline().split()
    for j in range(len(command)):
        command[j] = command[j][::-1]
        print(command[j], end=" ")
    print()
