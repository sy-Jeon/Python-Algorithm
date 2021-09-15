n = int(input())
growing_n = 0
count = 0

while True:
    count += 1
    growing_n = growing_n + count

    if n <= growing_n:
        break
    
print(growing_n)

# growing_n은 피보나치로 계속 더해진다.
# while문은 n보다 작을 떄 동안만 실행된다.