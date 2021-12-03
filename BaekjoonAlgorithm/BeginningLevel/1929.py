n = list(map(int, input().split()))

num = []
for i in range(n[0], n[1]+1):
    num.append(i)

check = 0
for i in range(len(num)+1):
    if num[i] % i == 0:
        check += 1
    
if check == 2:
    print(num[i])
