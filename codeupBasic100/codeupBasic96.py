# 바둑판 생성
column = []
for i in range(19):
    column.append([])
    # 바둑판 값 입력받음
    column_input = input().split()
    for j in range(19):
        column[i].append(int(column_input[j]))

# 총 개수와 x, y 좌표 입력받음
# get total number, x, y
n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x)-1, int(y)-1

    for j in range(19):
        if column[x][j] != 0:
            column[x][j] = 0
        else:
            column[x][j] = 1

        if column[j][y] != 0:
            column[j][y] = 0
        else:
            column[j][y] = 1

for i in range(19):
    for j in range(19):
        print(column[i][j], end=" ")
    print()