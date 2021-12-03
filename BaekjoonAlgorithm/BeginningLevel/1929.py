'''
Time over
'''
n = list(map(int, input().split()))

seq = []
index = 0
for i in range(n[0], n[1]+1):
    seq.append(i)
    check = 0
    for j in range(1, seq[index]+1):
        if seq[index] % j == 0:
            check += 1


    if check == 2:
        print(seq[index])

    index += 1
