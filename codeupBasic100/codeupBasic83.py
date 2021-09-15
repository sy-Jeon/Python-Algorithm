r, g, b = input().split()
r, g, b = int(r), int(g), int(b)
count = 0

for r_index in range(r):
    for g_index in range(g):
        for k_index in range(b):
            count += 1
            print(r_index, g_index, k_index)
print(count)


# 0 0 0 = 0
# 0 0 1 = 1
# 0 1 0 = 2
# 0 1 1 = 3
# 1 0 0 = 4
# 1 0 1 = 5
# 1 1 0 = 6
# 1 1 1 = 7
# 8