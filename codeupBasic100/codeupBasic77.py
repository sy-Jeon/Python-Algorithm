n = int(input())
even_num = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_num += i
print(even_num)