n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

s = a[0]
for i in range(n):
    if a[i] < s:
        s = a[i]
print(s)
