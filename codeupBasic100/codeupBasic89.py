a, r, n = input().split()
a, r, n = int(a), int(r), int(n)
goal_num = a

for i in range(2, n+1):
    goal_num *= r
print(goal_num)


# the other way
# a, r, n = input().split()
# a, r, n = int(a), int(r), int(n)
# goal_num = a
# count = 2

# while count <= n:
#     count += 1
#     goal_num *= r
# print(goal_num)