h, w = input().split()
h, w = int(h), int(w)
n = int(input())

column = []
for i in range(h+1):
    column.append([])
    print(column)
    for j in range(h+1):
        column[i].append(0)


for i in range(n):
    l, d, x, y = input().split()
    l, d, x, y = int(l), int(d), int(x)-1, int(y)-1
    
    for j in range(l):
        if d == 0:
            # 가로
            column[x][y] = 1
            y += 1
        else:
            # 세로
            column[x][y] = 1
            x += 1

for i in range(h):
    for j in range(h):
        print(column[i][j], end=" ")
    print()