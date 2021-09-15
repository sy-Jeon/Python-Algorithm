a, m, d, n = input().split()
a, m, d, n = int(a), int(m), int(d), int(n)
goal_num = a

for i in range(2, n+1):
    goal_num = goal_num * m + d
print(goal_num)
