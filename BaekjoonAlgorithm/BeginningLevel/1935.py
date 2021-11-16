import sys

count = int(input())
num = list(input())

num_list = [0] * count
for i in range(count):
    num_list[i] = int(sys.stdin.readline())

stack = []
for i in num:
    if i.isalpha():
        stack.append(num_list[ord(i) - ord("A")])

    else:
        b = stack.pop()
        a = stack.pop()
        
        if i == "*":
            c = a * b
        elif i == "/":
            c = a / b
        elif i == "+":
            c = a + b
        elif i == "-":
            c = a - b

        stack.append(c)

print("%.2f" %stack[-1])
