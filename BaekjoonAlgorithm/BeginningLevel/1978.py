n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(n):

    for j in range(2, a[i]):
        # print(a[i], "%", j)

        if a[i] % j != 0:
            print(a[i] % j)
            count += 1
            pass

print(count)
