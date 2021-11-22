c = ord("a")
t = ord('z')
alphabet = []
count = 0

while c <= t :
    alphabet.append(chr(c))
    c += 1
    count += 1

answer = [-1] * count

s = input()
location_count = -1

for i in s:
    for j in range(len(alphabet)):
        if i == alphabet[j]:
            location_count += 1
            if answer[j] <= -1:
                answer[j] = location_count

print(*answer)
