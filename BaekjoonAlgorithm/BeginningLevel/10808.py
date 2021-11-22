c = ord("a")
t = ord('z')
alphabet = []
count = 0

while c <= t :
    alphabet.append(chr(c))
    c += 1
    count += 1

answer = [0] * count

s = "baekjoon"

for i in s:
    for j in range(len(alphabet)):
        if i == alphabet[j]:
            answer[j] += 1

print(*answer)
