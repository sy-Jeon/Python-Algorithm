import sys

while True:
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break
    
    small, capital, num, space = 0, 0, 0, 0

    for i in range(len(s)):

        if 'a' <= s[i] <= 'z':
            small += 1

        elif 'A' <= s[i] <= 'Z':
            capital += 1
        
        elif s[i] <= ' ':
            space += 1

        elif s[i].isdigit():
            num += 1

    print(small, capital, num, space)
