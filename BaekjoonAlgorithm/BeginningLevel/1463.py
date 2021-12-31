import sys

read = sys.stdin.readline
N = int(read())

cache = [-1] * (N+3)
cache[1] = 0
cache[2] = cache[3] = 1

for i in range(4, N+1):
    cnt = 10**6
    if i % 3 == 0:
        cnt = min(cache[i//3], cnt)
    if i % 2 == 0:
        cnt = min(cache[i//2], cnt)
    
    cache[i] = min(cache[i-1], cnt) + 1
