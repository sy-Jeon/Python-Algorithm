# 1=1+0
# 3=2+1
# 6=3+3
# 10=4+6
# 15=5+10
# 21=6+15
# 28=7+21
# 36=8+28
# 45=9+36
# 55=10+45

# Fibonacci problem.
# Info.
# input: 54
# ouput: 10

# first way
n = 0
input_num = int(input())

for i in range(1, input_num+1):
    n = i + n
    if n >= input_num:
        print(i)
        break

# second way
# n = 0
# result = 0
# input_num = int(input())
# for i in range(1, input_num+1):
#     if n < input_num:
#         n = i + n
#         result = i
# print(result)

# third way
# n = int(input())
# s = 0
# t = 0
# while s<n:
#     t = t+1
#     s = s+t
# print(t)