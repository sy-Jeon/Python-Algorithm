# The greatest common divisor
# The leaste common multiple
n1, n2 = input().split()
a, b = int(n1), int(n2)

'''
way 1 ---------------------------------------------------
'''
while a % b > 0:
    a, b, c = b, a % b, a * b

print(b)
print(c // b)

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
