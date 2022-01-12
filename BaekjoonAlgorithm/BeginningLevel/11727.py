n = int(input())
arr = [0, 1, 3, 5]

for i in range(4, n+1):
   arr.append(arr[i-1] + arr[i-2] * 2)

print(arr[n] % 10007)
