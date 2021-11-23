'''
Modified code.
'''
s = input()

answer = [0] * 26

for i in s:
    answer[ord(i) - ord("a")] += 1

print(*answer)


# c = ord("a")
# t = ord('z')
# alphabet = []
# count = 0

# while c <= t :
#     alphabet.append(chr(c))
#     c += 1
#     count += 1

# answer = [0] * count

# s = input()

# for i in s:
#     for j in range(len(alphabet)):
#         if i == alphabet[j]:
#             answer[j] += 1

# print(*answer)
