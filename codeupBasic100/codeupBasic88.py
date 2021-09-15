a, d, n = input().split()
a, d, n = int(a), int(d), int(n)
goal_num = a
count = 2

while count <= n:
    count += 1
    goal_num += d
print(goal_num)


# the other way
# a,d,n=input().split()
# a=int(a)
# d=int(d)
# n=int(n)
# s=a
# for i in range(2, n+1):
# 	s+=d
# print(s)

#+3: 1  4   7   10  (13)    16  19  22  25
#+5: 1  6   11  16  (21)    26  31  36  41 
#+8: 1  9   17  25  (33)    41  49  57  65
#+3: 2  5   8   11  (14)