'''
Implement a queue that stores integers and then create a program that processes a given command as input.

There are a total of 6 orders.

Push X: Putting an integer X into a queue.
pop: subtract the preceding integer from the queue and output the number. If there is no integer in the queue, output -1.
size: Outputs an integer number in the queue.
empty: Output 1 or 0 if the queue is empty.
Front: Outputs an integer on the front of the queue. If there is no integer in the queue, output -1.
Back: Outputs an integer at the end of the queue. If there is no integer in the queue, output -1.
'''

import sys

n = int(input())
queue = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue[0])
            queue.pop(0)
        else:
            print("-1")
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if not queue:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif command[0] == "back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print("-1")
