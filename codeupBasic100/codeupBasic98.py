# 조건:
# 개미의 이동: 1순위. 오른쪽, 2순위. 아래쪽
# 개미의 출발선: (2, 2)

# 입력받을 때 2(먹이)의 x, y 좌표 값을 받는다.

feed_x, feed_y = 0, 0
# 미로 생성
m = []
for i in range(12):
    m.append([])
    # 미로 입력받음
    for j in range(12):
        m[i].append(0)

for i in range(10):
    m_input = input().split()
    for j in range(10):
        m[i+1][j+1] = int(m_input[j])
        # 먹이 위치 찾기
        if int(m_input[j]) == 2:
            feed_x, feed_y = i+1, j+1

x, y = 2, 2
while x != feed_x  or y != feed_y:
    m[x][y] = 9
    # 움직이기
    if m[x][y+1] != 1:
        y += 1
    else:
        x += 1

    if x < 10 and y < 10:
        m[x][y] = 9
    else:
        break

# 결과 출력
for i in range(1, 11):
    for j in range(1, 11):
        print(m[i][j], end=" ")
    print()
