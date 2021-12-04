m, n = map(int, input().split())

for i in range(m, n+1):
    if i > 1:
        if i % 2 == 0:
            if i == 2:
                print(i)
        elif i % 3 == 0:
            if i == 3:
                print(i)
        else:
            print(i)
            

'''
Time over

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
'''
