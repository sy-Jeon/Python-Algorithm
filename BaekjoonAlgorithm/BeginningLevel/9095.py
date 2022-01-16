total_n = int(input())
arr = [1, 2, 4]

for j in range(3, 10):
    arr.append(arr[j-1] + arr[j-2] + arr[j-3])

for i in range(total_n):
    n = int(input())
    print(arr[n-1])
