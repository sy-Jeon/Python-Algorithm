# 조건:
# 개미의 이동: 1순위. 오른쪽, 2순위. 아래쪽
# 개미의 출발선: (2, 2)

# 입력받을 때 2(먹이)의 x, y 좌표 값을 받는다.

feed_x, feed_y = 0, 0
# 미로 생성
mazemap = []
for i in range(10):
    mazemap.append([])
    # 미로 입력받음
    mazemap_input = input().split()
    for j in range(10):
        mazemap[i].append(int(mazemap_input[j]))
        # 먹이 위치 찾기
        if int(mazemap_input[j]) == 2:
            feed_x, feed_y = i, j

x, y = 1, 1
while x != feed_x  or y != feed_y:
    mazemap[x][y] = 9
    # 움직이기
    if mazemap[x][y+1] != 1:
        y += 1
    else:
        x += 1

    if x < 9 and y < 9:
        mazemap[x][y] = 9
    else:
        break

# 결과 출력
for i in range(10):
    for j in range(10):
        print(mazemap[i][j], end=" ")
    print()
