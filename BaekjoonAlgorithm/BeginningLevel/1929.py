m, n = map(int, input().split())

for i in range(m, n+1):
    if i <= 1:
        continue

    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
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
