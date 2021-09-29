'''
You are given a text that is a sequence of characters.
Cursor can be positioned inside of the text (between any two consecutive characters), at the beginning (left of the first character) or at the end (right of the last character) of the text.
You are given sequence of operations you must perform on the text. 

Possible operations are: 

L	move cursor one character to the left (if cursor is at the beginning, do nothing)
D	move cursor one character to the right (if cursor is at the end, do nothing)
B	delete character left of the cursor (if cursor is at the beginning, do nothing)
P $	add character $ right of the cursor

Time limit: 0.3 sec
'''

import sys

stack_l = list(input())
stack_r = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == "B" and stack_l:
        stack_l.pop()
    elif command[0] == "P":
        stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))


'''
Time Over Code
'''
# import sys

# text = list(input())
# n = int(input())
# cursor = len(text)

# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0] == "L" and cursor > 0:
#         cursor -= 1
#     elif command[0] == "D" and cursor < len(text):
#         cursor += 1
#     elif command[0] == "B" and cursor > 0:
#         text.pop(cursor-1)
#         cursor -= 1
#     elif command[0] == "P":
#         text.insert(cursor, command[1])
#         cursor += 1

# for i in range(len(text)):
#     print(text[i], end="")
