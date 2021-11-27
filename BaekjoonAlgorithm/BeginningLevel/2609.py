# The greatest common divisor
# The leaste common multiple
import sys
n1, n2 = map(int, sys.stdin.readline().split())
a, b = int(n1), int(n2)

'''
way 1 ---------------------------------------------------
'''
while b != 0:
    a = a % b
    a, b = b, a

print(a)
print(int(n1) * int(n2) // a)

'''
way 2 ---------------------------------------------------
'''
# import math

# print(math.gcd(a, b))
# print(math.lcm(a, b))

'''
way 3 ---------------------------------------------------
'''
# def gcd(a, b):
#     while a % b > 0:
#         c = a % b
#         a = b
#         b = c
#     return b

# def lcm(a, b):
#     return a * b // gcd(a, b)

# print(gcd(a, b))
# print(lcm(a, b))
