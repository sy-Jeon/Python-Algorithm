x = int(input())
n = list(map(int, input().split()))
# count = 0

# for i in range(n):

#     for j in range(2, x[i]):

#         print(x[i] % j)
#         if x[i] % j != 0:
#             count += 1

# print(count)

def primeNumbers(x, n):
    count = 0
    for i in range(x):

        for j in range(2, n[i]):
            print(n[i] % j)
            if n[i] % j == 0:
                return print("소수 아니야",n[i], "%", j,"=", n[i] % j)
        return print("소수 맞아")

primeNumbers(x, n)
