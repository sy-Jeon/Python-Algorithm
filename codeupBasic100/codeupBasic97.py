# h: height value of map
# w: width value of map
# n: additional number
# l: length
# d: direction (0: width ,1: height)

h, w = input().split()
h, w = int(h), int(w)
n = int(input())

# create map and set value 0 in the map
column = []
for i in range(h):
    column.append([])
    for j in range(w):
        column[i].append(0)

# get l, d, x, y value as value infomation
for i in range(n):
    l, d, x, y = input().split()
    l, d, x, y = int(l), int(d), int(x)-1, int(y)-1
    
    # If the direction value is 0, set the value 1 at the current location on the map and add 1 to y.
    for j in range(l):
        if d == 0:
            # width
            column[x][y] = 1
            y += 1
        else:
            # height
            column[x][y] = 1
            x += 1

# print the map
for i in range(h):
    for j in range(w):
        print(column[i][j], end=" ")
    print()
