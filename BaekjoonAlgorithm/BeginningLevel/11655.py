s = input()
answer = ''

for i in s:
    if i.islower():
            if 97 <= ord(i) <= 109:         #a-m
                answer += chr(ord(i) + 13)
            else:                           #n-z
                answer += chr(ord(i) - 13)
    elif i.isupper():
        if 65 <= ord(i) <= 77:              #A-M
            answer += chr(ord(i) + 13)
        else:                               #N-Z
            answer += chr(ord(i) - 13)
    else:
        answer += i

print(answer)
