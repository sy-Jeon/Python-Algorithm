column = []
for i in range(20):
    column.append([])
    for j in range(20):
        column[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    for j in range(n):
        column[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(column[i][j], end=" ")
    print()