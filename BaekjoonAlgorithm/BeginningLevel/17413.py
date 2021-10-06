text = list(input())
tag = 0
word = ''
result = ''

for i in text:

    if not tag:
        if i == '<':
            tag = 1
            word += i

        elif i == ' ':
            word += i
            result += word
            word = ''
        else:
            word = i + word

    elif tag:
        word += i
        if i == '>':
            tag = 0
            result += word
            word = ''
print(result + word)
