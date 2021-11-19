num = input()
answer = ''
stack = []

for i in num:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            # a+b*c 일 때 stack의 마지막 값이 + or -면 stack에는 *가 들어있지 않은 상태이기 때문에, answer에는 값이 [a, b, +]로 들어오게된다. 그렇기 때문에 *까지 스택에 쌓아야 answer에 값이 [a, b, c, *, +]로 들어오게 된다.
            while stack and stack[-1] == '+' and stack[-1] == '-':
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            # (a+b)일 때 stack의 마지막 값이 (면 stack에는 +가 들어있지 않은 상태이기 때문에, answer에는 값이 [a, (]로 들어오게된다. 그렇기 때문에 +까지 스택에 쌓아야 answer에 값이 [a, b, +]로 들어오게 된다.
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)
