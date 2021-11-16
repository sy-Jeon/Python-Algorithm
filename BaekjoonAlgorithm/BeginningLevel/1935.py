import sys

count = int(sys.stdin.readline())
num = list(sys.stdin.readline())

num_list = [0] * count
for i in range(count):
    num_list[i] = int(sys.stdin.readline())

stack = []
for i in num:
    if "A" <= i <= "Z":
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

print(format(stack[0], "%0.2f"))
