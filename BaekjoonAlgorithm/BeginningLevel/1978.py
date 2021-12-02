x = int(input())
n = list(map(int, input().split()))

count = 0
for i in range(x):

    check = 0
    for j in range(1, n[i]+1):
        if n[i] % j == 0:
            check += 1
        
    if check == 2:
        count += 1

print(count)
